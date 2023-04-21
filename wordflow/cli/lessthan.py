# lessthan.py
# ------------
# Compares the numbers at two different positions, and allows lines where the first
# number is less than the second. When --equal, equality is also allowed.

import re
import sys
from wordflow.pipe_guard import guard_pipe
from argparse import ArgumentParser

@guard_pipe
def main():
    parser = ArgumentParser()
    parser.add_argument('first', type=int, default=0)
    parser.add_argument('second', type=int, default=1)
    parser.add_argument('-e', '--equal', action='store_true')
    arguments = parser.parse_args()
    for line in sys.stdin:
        tokens = line.split()
        try: 
            a, b = float(tokens[arguments.first]), float(tokens[arguments.second])
        except IndexError:
            raise Exception(
                f"Tried to compare the numbers at positions {arguments.first} and" + 
                f"{arguments.second}, but there are only {len(tokens)} on the line: {line}"
            )
        except ValueError:
            raise ValueError(
                f"Couldn't read position {arguments.first} ({tokens[arguments.first]}) and " + 
                f"position {arguments.second} ({tokens[arguments.second]}) as numbers: {line}"
            )
        if a < b or (arguments.equal and a == b):
            sys.stdout.write(line)
