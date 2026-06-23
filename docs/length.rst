.. _length:

length
======

Prepends the length of a token to each line.

Usage
-----

.. code-block:: text

    length [position]

- ``position`` — which space-separated token to measure (default: ``0``).

Example
-------

::

    $ cat words.txt | length | head
    1 a
    2 aa
    3 aah

Combine with :ref:`order` to find the shortest or longest words in a list.
