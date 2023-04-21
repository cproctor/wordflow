# frequency.py
# ------------
# Returns the frequency (per billion words) of each word.

import sys
from wordflow.pipe_guard import guard_pipe
from argparse import ArgumentParser
import wordfreq

@guard_pipe
def main():
    parser = ArgumentParser()
    parser.add_argument('position', type=int, nargs='?', default=0)
    arguments = parser.parse_args()
    for line in sys.stdin:
        word = line.split()[arguments.position]
        freq = int(wordfreq.word_frequency(word, 'en') * 1e9)
        sys.stdout.write(str(freq) + ' ' + line)

