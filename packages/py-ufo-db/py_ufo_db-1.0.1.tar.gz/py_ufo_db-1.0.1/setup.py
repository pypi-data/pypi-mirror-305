from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py-ufo-db",
    version="1.0.1",
    author="Nazaryan Artem | Sl1dee36",
    author_email="spanishiwasc2@gmail.com",
    description="Python Unified Flexible Object Database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sl1dee36/pyufo-db",
    packages=find_packages(['py_ufo_db']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)