from setuptools import setup

__version__ = '1.0'
pybuf_classifiers = [
    'Programming Language :: Python :: 2',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities'
]
description = 'Modularize Protocol Buffer Compiler generated code for use within your package'


setup(
    name='pybuf',
    author='Marcus Medley',
    author_email='mdmeds@gmail.com',
    url='https://github.com/mdmedley/pybuf',
    version=__version__,
    py_modules=['pybuf'],
    install_requires=['protobuf'],
    description=description,
    long_description=description,
    license='MIT',
    classifiers=pybuf_classifiers)
