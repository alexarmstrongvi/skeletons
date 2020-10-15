================================================================================
Python project skeleton
================================================================================
Usage
-----


.. code-block:: bash

    $ setup_py_project ProjectName
    $ setup_py_project ProjectName --subpackages 3

.. code-block:: bash

    $ pylint skeletons/ tests/

.. code-block:: bash

    $ pydoc skeletons
    $ pydoc -w skeletons 
    $ pydoc -b

.. code-block:: bash

    $ sphinx

.. code-block:: bash

    $ python -m unittest tests/

.. code-block:: bash

    $ pytest tests/

.. code-block:: bash

    $ ./skeletons/runner.py foo.bar

References
----------
* Python project structure
   * `Real Python - "Python Application Layouts" <https://realpython.com/python-application-layouts/>`_ 

* Docstring formats
   * `Stack Overflow - "What is the standard Python docstring format?" <https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format>`_ - a good overview of ReST, Google, Numpydoc, and other docstring standards

* reStructuredText
   * `Online Sphinx Editor <https://livesphinx.herokuapp.com/>`_
   * `Online RST Editor <http://rst.ninjs.org/>`_ - Less helpful display but can convert to PDF
   * `Sphinx RST guide <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
   * `Official User Guide <https://docutils.sourceforge.io/rst.html>`_ - Examples don't display final output
* Project management tools
   * `Pylint <http://pylint.pycqa.org/en/latest/index.html>`_
   * `Pydoc <https://docs.python.org/3/library/pydoc.html>`_
