from setuptools import setup, Extension, Command
from Cython.Build import cythonize


SRC_DIR = "src"
PACKAGES = [SRC_DIR]

ext_foo = Extension(SRC_DIR + ".foo",
                  [SRC_DIR + "/foo.pyx"]
                  )

ext_meta = Extension(SRC_DIR + ".metafoo",
                  [SRC_DIR + "/metafoo.pyx"]
                  )

EXTENSIONS = cythonize([ext_foo, ext_meta])

setup(
    name = 'minimalcriminal',
    packages=PACKAGES,
    ext_modules=EXTENSIONS
)
