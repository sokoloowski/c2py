from setuptools import setup, find_packages


setup(
    name="c2py",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime",
        "autopep8",
        "pytest"
    ]
)
