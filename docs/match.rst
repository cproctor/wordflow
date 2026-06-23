.. _match:

match
=====

Allows through only the lines whose token matches a regular expression.

Usage
-----

.. code-block:: text

    match pattern [position]

- ``pattern`` — a regular expression to search for.
- ``position`` — which space-separated token to check (default: ``0``).

Example
-------

Find words containing a doubled vowel::

    $ cat words.txt | match "aa|ee|ii|oo|uu"

Regular expressions often contain characters with special meaning to the
shell (like ``|``), so it's safest to wrap the pattern in quotation marks.
