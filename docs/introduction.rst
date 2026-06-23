.. _introduction:

Introduction
============

Every program on the command line has three streams: standard in, standard
out, and standard error. A program reads its input from standard in, and
writes its results to standard out. The UNIX pipe operator, ``|``, connects
one program's standard out to the next program's standard in, letting you
build up a complex transformation out of small, simple pieces. `Wordflow`
provides a set of small programs, each of which does one thing, so that you
can chain them together with pipes to explore and transform lists of words.

Each `Wordflow` utility reads lines of space-separated tokens from standard
in and writes lines to standard out. This makes it possible to feed the
output of one utility directly into the next.

Getting a word list
--------------------

To experiment with these utilities, you'll want a file containing a list of
words, one per line. If you installed `Wordflow` as part of `Making With
Code`, you already have access to a list of 370,000 English words
(``words_370k.txt``) bundled with the package. You can also use any other
plain-text word list, such as the dictionary built into UNIX and Linux
systems.

A first pipeline
-----------------

Here's a simple example. ``cat`` prints the contents of a file to standard
out, so ``cat words.txt`` writes every word in the file, one per line. We can
pipe that into ``head`` to see just the first few lines::

    $ cat words.txt | head

Filtering with ``match``
-------------------------

:ref:`match` allows through only the lines whose word matches a regular
expression. For example, to find words containing a doubled vowel::

    $ cat words.txt | match "aa|ee|ii|oo|uu" | count

Regular expressions often need to be wrapped in quotation marks so the shell
doesn't try to interpret special characters itself. The ``^`` and ``$``
anchors are especially useful: ``^a`` matches words that start with "a", and
``e$`` matches words that end with "e".

Adding information with ``length``, ``frequency``, ``unique``, and ``put``
----------------------------------------------------------------------------

Several `Wordflow` utilities prepend a new piece of information to each
line, so that later utilities in the pipeline can sort or filter on it:

- :ref:`length` prepends the length of the word.
- :ref:`frequency` prepends the word's frequency, in occurrences per billion
  words of English text.
- :ref:`unique` prepends the sorted, unique letters used in the word.
- :ref:`put` prepends a fixed number you supply, the same for every line.

For example, to see how long each word is::

    $ cat words.txt | length | head
    1 a
    2 aa
    3 aah
    4 aahed
    ...

Sorting with ``order``
-----------------------

:ref:`order` sorts lines by the token at a given position. When that token
looks like a number, it sorts numerically; otherwise, it sorts
alphabetically. Combining ``frequency`` and ``order`` lets us find the most
common words. Since ``frequency`` prepends the frequency as position 0 and
the word itself ends up at position 1, we can pull just the word back out
with :ref:`pluck`::

    $ cat words.txt | frequency | order -r | pluck 1 | head -n 1000 > common_1000.txt

This builds the 1,000 most common words in the list and saves them to a new
file with the ``>`` redirection operator. Changing ``head -n 1000`` to
``head -n 10000`` or ``head -n 100000`` gives the 10,000 or 100,000 most
common words instead.

Comparing positions with ``equal`` and ``lessthan``
------------------------------------------------------

:ref:`equal` and :ref:`lessthan` compare the numbers found at two positions
on a line, letting through only the lines where the comparison holds. This
is most useful after you've prepended more than one piece of information.
For example, to find the most common ten-letter words, we first prepend the
length of each word, keep only the words of length 10, then prepend the
frequency, sort, and pull out just the word::

    $ cat words.txt | length | put 10 | equal | frequency 2 | order -r | pluck 3 | head

Here, ``length`` prepends the word's length at position 0, pushing the word
itself to position 1. ``put 10`` prepends the literal number 10 at position
0, pushing the length to position 1 and the word to position 2. ``equal``
(using its defaults, positions 0 and 1) then keeps only the lines where the
10 we added equals the word's length — in other words, the ten-letter
words. Finally, ``frequency 2`` looks up the frequency of the token at
position 2 (the word) and prepends it, pushing the word out to position 3,
which is why the pipeline ends with ``pluck 3``. Once a pipeline has several
prepended columns, it helps to write out, on paper, what each position
holds at each stage.

Counting with ``count``
-------------------------

:ref:`count` is the simplest utility of all: it counts how many lines arrive
on standard in, and prints that single number. It's especially handy at the
end of a pipeline built with :ref:`match`, to answer questions like "how
many words contain two vowels in a row?"

Putting it together
--------------------

Each of these utilities does one small job. The power of `Wordflow` comes
from composing them with pipes into longer pipelines, the same way you might
compose function calls in Python. The :ref:`api` describes every utility's
arguments in detail.
