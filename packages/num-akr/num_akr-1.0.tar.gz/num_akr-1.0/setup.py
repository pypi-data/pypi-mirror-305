from setuptools import setup, find_packages

VERSION = '1.0'

setup(
    name="num_akr",
    version=VERSION,
    author="Ameba",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy', 'pyperclip']
)