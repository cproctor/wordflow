# sort.py
# --------
# Sorts lines, using a specific token from each line
# If the tokens are all numeric, sorts numerically.

import re
import sys
from wordflow.pipe_guard import guard_pipe
from argparse import ArgumentParser

def is_float(string):
    pattern = "^\-?[0-9]+(\.[0-9]+)?$"
    return bool(re.match(pattern, string))

@guard_pipe
def main():
    parser = ArgumentParser()
    parser.add_argument('position', type=int, nargs='?', default=0)
    parser.add_argument('-r', '--reverse', action='store_true')
    arguments = parser.parse_args()
    lines = [line for line in sys.stdin]
    keys = [line.split()[arguments.position] for line in lines]
    if all([key.isnumeric() for key in keys]):
        keys = [int(key) for key in keys]
    elif all([is_float(key) for key in keys]):
        keys = [float(key) for key in keys]
    sorted_lines = [line for key, line in sorted(zip(keys, lines), reverse=arguments.reverse)]
    for line in sorted_lines:
        sys.stdout.write(line)
