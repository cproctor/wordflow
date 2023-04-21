# filter.py
# ------------
# Filters text from stdin. Lines matching `pattern` are sent to stdout.

import re
import sys
from wordflow.pipe_guard import guard_pipe
from argparse import ArgumentParser

@guard_pipe
def main():
    parser = ArgumentParser()
    parser.add_argument('pattern')
    parser.add_argument('position', type=int, nargs='?', default=0)
    arguments = parser.parse_args()
    for line in sys.stdin:
        tokens = line.split()
        if re.search(arguments.pattern, tokens[arguments.position]):
            sys.stdout.write(line)
