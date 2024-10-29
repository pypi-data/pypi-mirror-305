.. -*- mode: rst -*-

|AppVeyor|_ |Codecov|_ |ReadTheDocs|_ |PythonVersion|_ |Pypi|_

.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/pvkh4hic8rpxcoyn?svg=true
.. _AppVeyor: https://ci.appveyor.com/project/paris-saclay-cds/specio/history

.. |Codecov| image:: https://codecov.io/gh/paris-saclay-cds/specio/branch/master/graph/badge.svg
.. _Codecov: https://codecov.io/gh/paris-saclay-cds/specio

.. |ReadTheDocs| image:: https://readthedocs.org/projects/specio/badge/?version=latest
.. _ReadTheDocs: http://specio.readthedocs.io/en/latest/?badge=latest

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/specio-py310.svg
.. _PythonVersion: https://pypi.org/project/specio-py310/

.. |Pypi| image:: https://badge.fury.io/py/specio-py310.svg
.. _Pypi: https://pypi.org/project/specio-py310/

specio-py310
============

specio-py310 is a library which allows to easily open spectroscopic format currently
available. It is widely inspired by the `imageio <https://github.com/imageio/imageio>`__ architecture.

Documentation
-------------

Installation documentation, API documentation, and examples can be found on the
documentation_.

.. _documentation: http://specio.readthedocs.io/

Installation
------------

Dependencies
~~~~~~~~~~~~

The following dependencies are mandatory:

* numpy
* six

In addition, there is the following optional dependencies
required by some readers and to export into CSV:

* pandas
* spc
* pyopenms

You can install all these dependencies via pip::

    pip install -r requirements.txt

User installation
~~~~~~~~~~~~~~~~~

You can install the package using pip and the PyPi repository::

    pip install -U specio-py310

Alternatively, you can clone it and run the setup.py file. Use the following
commands to get a copy from Github and install::

    git clone https://github.com/BjornMelin/specio-py310.git
    cd specio-py310
    pip install .

You can also install the master branch directly with pip::

    pip install git+https://github.com/BjornMelin/specio-py310.git
