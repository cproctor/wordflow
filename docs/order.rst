.. _order:

order
=====

Sorts lines by the token at a given position. If every value at that
position looks like a number, lines are sorted numerically; otherwise,
they're sorted alphabetically.

Usage
-----

.. code-block:: text

    order [position] [-r | --reverse]

- ``position`` — which space-separated token to sort by (default: ``0``).
- ``-r``, ``--reverse`` — sort in descending order instead of ascending.

Example
-------

::

    $ cat words.txt | length | order | head

Sorts words by length, shortest first. Add ``-r`` to see the longest words
first instead.
