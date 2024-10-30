from setuptools import setup, find_packages

setup(
    name="blexus",
    version="0.0.6",
    author="Blexus",
    author_email="mmmmmm505090@gmail.com",
    description="Blexus official package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Blexus-org/pkg",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
