# pluck.py
# --------
# Plucks a token at the given position from each line

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
        print(tokens[arguments.position])
