.. _equal:

equal
=====

Compares the numbers at two positions on each line, and allows through only
the lines where the two numbers are equal.

Usage
-----

.. code-block:: text

    equal [first] [second]

- ``first`` — position of the first number to compare (default: ``0``).
- ``second`` — position of the second number to compare (default: ``1``).

Example
-------

After prepending a word's length and a fixed number with :ref:`length` and
:ref:`put`, ``equal`` keeps only the lines where the two match, i.e. words
of that exact length::

    $ cat words.txt | length | put 10 | equal
