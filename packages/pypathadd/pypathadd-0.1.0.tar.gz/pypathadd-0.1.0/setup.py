# -*- coding: utf-8 -*-
# @Author: Simon Walser
# @Date:   2024-11-01 14:52:55
# @Last Modified by:   Simon Walser
# @Last Modified time: 2024-11-01 15:42:42

from setuptools import setup, find_packages

setup(
    name="pypathadd",
    version="0.1.0",
    author="Simon Walser",
    description="A utility to append all folders and subfolders of the root directory to the Python path.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AIGR-sw/pypathadd",  # replace with the actual URL
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)