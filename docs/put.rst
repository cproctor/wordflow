.. _put:

put
===

Prepends a fixed number to every line.

Usage
-----

.. code-block:: text

    put number

- ``number`` — the number to prepend to every line. If it's a whole
  number, it's written without a decimal point.

Example
-------

::

    $ cat words.txt | put 10 | head
    10 a
    10 aa
    10 aah
    ...

This is most useful for comparing against a value computed elsewhere in a
pipeline, using :ref:`equal` or :ref:`lessthan`.
