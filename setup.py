from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [Extension("information_gain_cy", ["information_gain_cy.pyx"])]

setup(name='epmgp',
      version='1.0',
      ext_modules = cythonize(ext_modules),
      description='',
      author='',
      author_email='',
      url='',
      classifiers= ['Programming Language :: Python',],
     )
