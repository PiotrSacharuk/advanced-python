# setup.py
from setuptools import setup
from Cython.Build import cythonize

# python setup.py build_ext --inplace
setup(ext_modules = cythonize("primes_cy.pyx", compiler_directives={'language_level': "3"}))
