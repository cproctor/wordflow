.. _unique:

unique
======

Prepends the sorted, unique letters used in a token.

Usage
-----

.. code-block:: text

    unique [position]

- ``position`` — which space-separated token to inspect (default: ``0``).

Example
-------

::

    $ echo "mississippi" | unique
    imps mississippi

This is handy for finding words built from a limited set of letters, or for
spotting words with no repeated letters at all (where the unique-letters
string is as long as the word itself).
