from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='hescheme',
    version='0.1',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'run_he = main:main',
        ]
    },
    package_dir={'': 'src'},
    author='Mădălina Bolboceanu',
    author_email='madalinabolboceanu@gmail.com',
)
