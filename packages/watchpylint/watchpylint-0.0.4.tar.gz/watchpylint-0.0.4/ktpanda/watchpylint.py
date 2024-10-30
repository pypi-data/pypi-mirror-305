#!/usr/bin/python3
# PYTHON_ARGCOMPLETE_OK

# watchpylint
#
# Copyright (C) 2022 Katie Rust (katie@ktpanda.org)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#!/usr/bin/python3
import sys
import re
import time
import argparse
import subprocess
import asyncio
from pathlib import Path
from collections import defaultdict

import argcomplete

VERSION = "0.0.4"

IN_PROGRESS = '<lint in progress>\n'
COMPLETE = '<lint complete>'

RX_LINT_LINE = re.compile(r':\d+:.*([EWRC]\d+):.*\s*$')

PRIO_MAP = {
    'E': 0,
    'W': 1,
    'R': 2,
    'C': 3
}

class FileTracker:
    def __init__(self, path):
        self.path = path
        self.module = str(path.with_suffix('')).replace('/', '.')
        self.mtime = 0
        self.linttask = None
        self.output = None

    def check(self):
        try:
            new_mtime = self.path.stat().st_mtime
        except OSError:
            new_mtime = 0
        change = new_mtime != self.mtime
        self.mtime = new_mtime
        return change

class LintWatcher:
    def __init__(self, files, output, rcfile=None):
        self.output = output
        self.baseargs = ['pylint']
        if rcfile:
            self.baseargs.append(f'--rcfile={rcfile}')
        self.trackers = [FileTracker(path) for path in files]

    async def run_pylint(self, tracker):
        pylint_args = list(self.baseargs)
        pylint_args.append(tracker.module)
        proc = await asyncio.create_subprocess_exec(*pylint_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = await proc.communicate()
        await proc.wait()

        tracker.output = messages = defaultdict(list)
        for line in out.decode('utf8', 'ignore').splitlines():
            m = RX_LINT_LINE.search(line)
            if m:
                messages[m.group(1)].append(line)

        tracker.linttask = None
        print(f' ... lint {tracker.path} complete')

    def collect_messages(self):
        all_messages = defaultdict(list)
        for tracker in self.trackers:
            if tracker.output:
                for msgtype, lines in tracker.output.items():
                    all_messages[msgtype].extend(lines)

        with self.output.open('w', encoding='utf8') as fp:
            for _, lines in sorted(all_messages.items(), key=lambda t: (PRIO_MAP.get(t[0][:1], 10), t[0])):
                for line in lines:
                    print(line, file=fp)
                print(file=fp)
            print(COMPLETE, file=fp)

    def clear_messages(self):
        with self.output.open('w', encoding='utf8') as fp:
            fp.write(IN_PROGRESS)


    async def run(self):
        active_tasks = set()
        while True:
            for tracker in self.trackers:
                if tracker.check():
                    if len(active_tasks) >= 8:
                        break
                    print(f'Detected changes in {tracker.path}')
                    self.clear_messages()
                    tracker.linttask = asyncio.create_task(self.run_pylint(tracker))
                    active_tasks.add(tracker.linttask)

            if active_tasks:
                _, active_tasks = await asyncio.wait(active_tasks, timeout=0.5, return_when=asyncio.FIRST_COMPLETED)
                if not active_tasks:
                    print()
                    print('All lint processes complete')
                    print()
                    self.collect_messages()

            else:
                await asyncio.sleep(0.25)

def main():
    p = argparse.ArgumentParser(prog='watchpylint', description=f'watchpylint version {VERSION}')
    p.add_argument('files', nargs='*', type=Path, help='Python files to watch and lint')
    p.add_argument('-V', '--version', action='version', version=f'%(prog)s {VERSION}')
    p.add_argument('-o', '--output', metavar="PATH", type=Path, default=Path('lint.txt'), help='Output path (default: %(default)s)')
    p.add_argument('-r', '--rcfile', metavar="PATH", type=Path, help='Pylint configuration file')
    p.add_argument('-w', '--wait', metavar="PATH", type=Path, help='Wait for lint to complete and write output to PATH')
    argcomplete.autocomplete(p)
    args = p.parse_args()

    if args.wait:
        endtime = time.time() + 30
        while time.time() < endtime:
            text = args.wait.read_text(encoding='utf8')

            if COMPLETE not in text[-20:]:
                time.sleep(.25)
            else:
                parent = args.wait.parent
                for line in text.split('\n'):
                    fn, sep, rest = line.partition(':')
                    if sep:
                        line = f'{parent / fn}{sep}{rest}'
                    print(line)

                return 0

        print('Timed out waiting for lint to complete')
        return 1

    if not args.files:
        p.print_help()
        return 0

    lw = LintWatcher(args.files, args.output, args.rcfile)
    return asyncio.run(lw.run())

if __name__ == '__main__':
    sys.exit(main())
