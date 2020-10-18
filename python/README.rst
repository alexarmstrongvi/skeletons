================================================================================
Python project skeleton
================================================================================
Usage
-----

To setup a new project:

.. code-block:: bash

    $ setup_py_project ProjectName
    $ setup_py_project ProjectName --subpackages 3

To run the linter:

.. code-block:: bash

    $ pylint --generate-rcfile > current_pylintrc
    $ pylint skeletons/ tests/

To glance at the documentation:

.. code-block:: bash

    $ pydoc skeletons
    $ pydoc -b

To generate the full documentation

.. code-block:: bash

    $ cd docs
    $ make html
    $ open build/html/index.html

To run tests :

.. code-block:: bash

    $ python -m doctest skeletons/subpackage1/submodule1.py
    $ py.test --doctest-modules skeletons
    $ pytest tests/

To run the packages main script:

.. code-block:: bash

    $ ./skeletons/runner.py
    $ ./skeletons/runner.py -i data/input.json -o data/output.txt -l DEBUG

References
----------
* Python project structure
    * `Real Python - "Python Application Layouts" <https://realpython.com/python-application-layouts/>`_ 
* Development and debugging tools
    * `Pylint <http://pylint.pycqa.org/en/latest/index.html>`_
    * `Pydoc <https://docs.python.org/3/library/pydoc.html>`_
    * Doctest
    * Unittest
    * Pytest

