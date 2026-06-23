.. _lessthan:

lessthan
========

Compares the numbers at two positions on each line, and allows through only
the lines where the first number is less than the second.

Usage
-----

.. code-block:: text

    lessthan [first] [second] [-e | --equal]

- ``first`` — position of the first number to compare (default: ``0``).
- ``second`` — position of the second number to compare (default: ``1``).
- ``-e``, ``--equal`` — also allow lines where the two numbers are equal.

Example
-------

Keep only lines where the first number is smaller than the second::

    $ cat scores.txt | lessthan 0 1

Raises an error if either position isn't a number, or if a line doesn't
have enough tokens to read both positions.
