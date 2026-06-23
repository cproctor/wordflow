.. _frequency:

frequency
=========

Prepends the approximate frequency of a word in English text, measured in
occurrences per billion words.

Usage
-----

.. code-block:: text

    frequency [position]

- ``position`` — which space-separated token to look up (default: ``0``).

Example
-------

::

    $ cat words.txt | frequency | order -r | pluck 1 | head -n 1000

This finds the 1,000 most common words: prepend each word's frequency,
sort by frequency in reverse (most frequent first), then pull just the
word back out with :ref:`pluck`.
