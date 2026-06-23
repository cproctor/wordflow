.. _pluck:

pluck
=====

Replaces each line with just the token at the given position, discarding
the rest of the line.

Usage
-----

.. code-block:: text

    pluck [position]

- ``position`` — which space-separated token to keep (default: ``0``).

Example
-------

After prepending extra information with utilities like :ref:`length` or
:ref:`frequency`, use ``pluck`` to throw away everything except the
original word::

    $ cat words.txt | frequency | order -r | pluck 1 | head -n 1000
