from setuptools import setup, find_packages
from pathlib import Path

# Read the content of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='jadugar',
    version='0.7',  # Update the version number
    packages=find_packages(),
    include_package_data=True,
    package_data={'file': ['../data/*.txt']},
    install_requires=[
        # list your dependencies here
    ],
    author='Raj N',
    url='https://github.com/rajnandale',
    description='Jadugar is a fun project for experimentation with Python packages, read more at project links below',
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={ 
        'GitHub': 'https://github.com/rajnandale',
        'Gist': 'https://gist.github.com/rajnandale/471c9f2fe5e6012b5fdd8990ef761239',
        'LinkedIn': 'https://www.linkedin.com/in/rajnandale',
    },
)
