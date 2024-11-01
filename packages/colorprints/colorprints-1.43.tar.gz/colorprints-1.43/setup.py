from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="colorprints",
    version="1.43",
    packages=find_packages(),
    description="Simple Color Prints library made as classwork",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        #none
        ],
)
