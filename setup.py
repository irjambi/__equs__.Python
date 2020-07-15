modifiction


"""
Setup file for the example_module
"""
from setuptools import setup

setup(
    name='example_package',
    version='0.1',
    description='An example Python module',
    author='Markus Rambach',
    author_email='m.rambach@uq.edu.au',
    packages=['problems'],
    install_requires=['numpy', 'scipy', 'qinfer']
)
