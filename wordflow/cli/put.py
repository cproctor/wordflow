# put.py
# -----------
# Prepends the number to each line.

import sys
from wordflow.pipe_guard import guard_pipe
from argparse import ArgumentParser

@guard_pipe
def main():
    parser = ArgumentParser()
    parser.add_argument('number', type=float)
    arguments = parser.parse_args()
    if arguments.number == int(arguments.number):
        number = int(arguments.number)
    else:
        number = arguments.number
    for line in sys.stdin:
        sys.stdout.write(str(number) + ' ' + line)

