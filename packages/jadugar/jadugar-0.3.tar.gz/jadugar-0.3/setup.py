# setup.py

from setuptools import setup, find_packages

setup(
    name='jadugar',
    version='0.3',  # Update the version number
    packages=find_packages(),
    include_package_data=True,
    package_data={'file': ['../data/*.txt']},
    install_requires=[
        # list your dependencies here
    ],
    author='Raj Nandale',
    author_email='kkwieer@yahoo.com',
    description='this is simple usage : "from file.file2 import read_file \n data = read_file("doc2.ipynb")"',
)
