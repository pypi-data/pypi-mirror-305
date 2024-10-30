# This file is used to package the log module for distribution.
from setuptools import setup, find_packages

setup(
    name="sdutilities-log",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "tqdm",
    ],
    author="Stephen Olsen, Taylor Ward, McKenna Magoffin, Jaffar Shaik, Evan Tucker, Chintan Dalal",
    author_email="taylorward@sociallydetermined.com, \
                  mckennamagoffin@sociallydetermined.com, \
                  chintandalal@sociallydetermined.com",
    maintainer="Chintan Dalal",
    maintainer_email="chintandalal@sociallydetermined.com",
    description="This package is intended to implement uniformity across \
                 SD Data Science projects. This module is intended to replace the deprecated `SDLogger` class in future versions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SociallyDetermined/sdutilities_package/sdutilities/log",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)