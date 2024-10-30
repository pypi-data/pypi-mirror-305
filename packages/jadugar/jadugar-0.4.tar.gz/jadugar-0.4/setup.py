# setup.py

from setuptools import setup, find_packages

setup(
    name='jadugar',
    version='0.4',  # Update the version number
    packages=find_packages(),
    include_package_data=True,
    package_data={'file': ['../data/*.txt']},
    install_requires=[
        # list your dependencies here
    ],
    author='Raj N',
    author_email='mail6164@duck.com',
    description='Jadugar is fun project for experimentation with python packages, read more at url ',
    url='https://gist.github.com/rajnandale/471c9f2fe5e6012b5fdd8990ef761239.js'
)
