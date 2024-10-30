from setuptools import setup, find_packages
from pathlib import Path

# Read the content of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='jadugar',
    version='0.6',  # Update the version number
    packages=find_packages(),
    include_package_data=True,
    package_data={'file': ['../data/*.txt']},
    install_requires=[
        # list your dependencies here
    ],
    author='Raj N',
    author_email='mail6164@duck.com',
    description='Jadugar is a fun project for experimentation with Python packages, read more at project links below',
    long_description=long_description,  # Including the README as the long description
    long_description_content_type='text/markdown',  # This ensures markdown rendering on PyPI
    url='https://gist.github.com/rajnandale/471c9f2fe5e6012b5fdd8990ef761239'
)
