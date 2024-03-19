import os
from glob import glob
import sys
from setuptools import setup, find_packages
import boto3
import ast


def read(fname):
    """
    Args:
      fname:
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_version():
    return read("VERSION").strip()


setup(
    name="A Sample Tool",
    version=read_version(),
    description="A tool to do the modularization and run the codes as a package",
    url="https://www.google.com",
    author="Abhishek Prajapati",
    author_email="abhishekiitr999@gmail.com",
    maintainer_email="abhishekiitr999@gmail.co",
    license="NA",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[
        os.path.splitext(os.path.basename(path))[0] for path in glob("src/*.py")
    ],
    install_requires=[
        "importlib_metadata",
        "matplotlib>=3.5.1",
        "numpy>=1.21.4",
        "pandas>=1.3.5",
        "boto3>=1.18.45",
        "statsmodels>=0.13.1",
        "s3fs>=0.4.2",
        "seaborn>=0.11.2",
        "scikit-learn",
        "scipy",
        "jinja2"
    ],
    zip_safe=False,
    include_package_data=True,
)

