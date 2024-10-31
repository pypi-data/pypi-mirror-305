from setuptools import setup, find_packages

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Just DNA Module'


setup(
    name="just-dna-module",
    version=VERSION,
    author="Anton Kulaga",
    author_email="antonkulaga@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        "oakvar",
        # add any other dependencies here
    ],
    python_requires=">=3.11",  # adjust minimum Python version as needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # adjust license as needed
        "Operating System :: OS Independent",
    ],
)
