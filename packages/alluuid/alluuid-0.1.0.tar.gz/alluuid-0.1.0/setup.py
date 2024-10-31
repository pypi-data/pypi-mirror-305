# setup.py
from setuptools import setup, find_packages

setup(
    name="alluuid",
    version="0.1.0",
    author="Krishna Tadi",
    author_email="er.krishnatadi@gmail.com",
    description="AllUUID is a versatile Python library for generating universally unique identifiers (UUIDs). It supports multiple versions of UUIDs, including version 1 (time-based), version 4 (random), and version 7 (timestamp-based). This tool is ideal for developers looking to create unique identifiers for databases, session tokens, or any other use cases where uniqueness is critical.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/krishnatadi/alluuid",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
