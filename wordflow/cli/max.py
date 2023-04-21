# max.py
# ------------
# Filters text from stdin, comparing the token at the specified position 
# against `value`.

import re
import sys
from wordflow.pipe_guard import guard_pipe
from argparse import ArgumentParser

@guard_pipe
def main():
    parser = ArgumentParser()
    parser.add_argument('value', type=float)
    parser.add_argument('position', type=int, nargs='?', default=0)
    arguments = parser.parse_args()
    for line in sys.stdin:
        tokens = line.split()
        if float(tokens[arguments.position]) <= arguments.value:
            sys.stdout.write(line)
