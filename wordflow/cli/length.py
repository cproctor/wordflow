# length.py
# -----------
# Prepends the length of the selected token to each string in stdin.

import sys
from wordflow.pipe_guard import guard_pipe
from argparse import ArgumentParser

@guard_pipe
def main():
    parser = ArgumentParser()
    parser.add_argument('position', type=int, nargs='?', default=0)
    arguments = parser.parse_args()
    for line in sys.stdin:
        tokens = line.split()
        token_length = len(tokens[arguments.position])
        sys.stdout.write(str(token_length) + ' ' + line)
