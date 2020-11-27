from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Homomorphic Encryption Scheme',
    version='0.1',
    install_requires=requirements,
    author='Mădălina Bolboceanu',
)
