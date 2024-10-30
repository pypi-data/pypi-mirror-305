html5rdf
========

.. image:: https://github.com/html5lib/html5lib-python/actions/workflows/python-tox.yml/badge.svg
    :target: https://github.com/html5lib/html5lib-python/actions/workflows/python-tox.yml

html5rdf is a pure-python library for parsing HTML to DOMFragment objects for the use in RDFLib.
html5rdf is a fork of html5lib-python. See below for the html5lib README.

----

It is designed to conform to the WHATWG HTML specification, as is implemented by all major
web browsers.

htm5lib-modern is designed as a drop-in replacement for ``html5lib`` that exposes a new
``html5lib`` module without Python 2 support and without the legacy dependencies on
``six``, and ``webencodings``. Note, you should not have the old deprecated ``html5lib``
and ``html5lib-modern`` in your dependency tree at the same time, because they alias.


Usage
-----

Simple usage follows this pattern:

.. code-block:: python

  import html5rdf
  with open("mydocument.html", "rb") as f:
      document = html5rdf.parse(f)

or:

.. code-block:: python

  import html5rdf
  document = html5rdf.parse("<p>Hello World!")

By default, the ``document`` will be an ``xml.etree`` element instance.
Whenever possible, html5lib chooses the accelerated ``ElementTree``
implementation.

Two other tree types are supported: ``xml.dom.minidom`` and
``lxml.etree``. To use an alternative format, specify the name of
a treebuilder:

.. code-block:: python

  import html5rdf
  with open("mydocument.html", "rb") as f:
      lxml_etree_document = html5rdf.parse(f, treebuilder="lxml")

When using with ``urllib.request`` (Python 3), the charset from HTTP
should be pass into html5rdf as follows:

.. code-block:: python

  from urllib.request import urlopen
  import html5rdf

  with urlopen("http://example.com/") as f:
      document = html5rdf.parse(f, transport_encoding=f.info().get_content_charset())

To have more control over the parser, create a parser object explicitly.
For instance, to make the parser raise exceptions on parse errors, use:

.. code-block:: python

  import html5rdf
  with open("mydocument.html", "rb") as f:
      parser = html5rdf.HTMLParser(strict=True)
      document = parser.parse(f)

When you're instantiating parser objects explicitly, pass a treebuilder
class as the ``tree`` keyword argument to use an alternative document
format:

.. code-block:: python

  import html5rdf
  parser = html5rdf.HTMLParser(tree=html5rdf.getTreeBuilder("dom"))
  minidom_document = parser.parse("<p>Hello World!")

More documentation is available at https://html5lib.readthedocs.io/.


Installation
------------

html5rdf works on CPython 3.8+ and PyPy. To install:

.. code-block:: bash

    $ pip install html5rdf

The goal is to support a (non-strict) superset of the versions that `pip
supports
<https://pip.pypa.io/en/stable/installing/#python-and-os-compatibility>`_.


Optional Dependencies
---------------------

The following third-party libraries may be used for additional
functionality:

- ``lxml`` is supported as a tree format (for both building and
  walking) under CPython (but *not* PyPy where it is known to cause
  segfaults);

- ``genshi`` has a treewalker (but not builder); and

- ``chardet`` can be used as a fallback when character encoding cannot
  be determined.


Bugs
----

Please report any bugs on the `issue tracker
<https://github.com/html5lib/html5lib-python/issues>`_.


Tests
-----

Unit tests require the ``pytest`` and ``mock`` libraries and can be
run using the ``pytest`` command in the root directory.

Test data are contained in a separate `html5lib-tests
<https://github.com/html5lib/html5lib-tests>`_ repository and included
as a submodule, thus for git checkouts they must be initialized::

  $ git submodule init
  $ git submodule update

If you have all compatible Python implementations available on your
system, you can run tests on all of them using the ``tox`` utility,
which can be found on PyPI.

