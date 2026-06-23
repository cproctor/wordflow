.. _count:

count
=====

Counts how many lines arrive on standard in, and prints that single number.
Takes no arguments.

Usage
-----

.. code-block:: text

    count

Example
-------

How many words contain two vowels in a row?

::

    $ cat words.txt | match "aa|ee|ii|oo|uu" | count
