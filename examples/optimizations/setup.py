from setuptools import setup
from Cython.Build import cythonize

# python3 setup.py build_ext --inplace
setup(ext_modules=cythonize("primes_c.pyx"))
