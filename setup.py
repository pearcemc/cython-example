from setuptools import setup, Extension, Command
from Cython.Build import cythonize

setup(
    name = 'streams',
    ext_modules = cythonize("*.pyx")
)
