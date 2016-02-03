from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# see example at https://github.com/pypa/sampleproject/blob/master/setup.py
setup(
    name='pythonworkflow',
    version='0.1.0',
    description='Attempting to figure out Python packages',
    long_description=long_description,
    url='https://github.com/porglezomp-misc/python-workflow',
    author='Caleb Jones',
    author_email='self@calebjones.net',
    license='None',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='sample',
    packages=find_packages(),
)
