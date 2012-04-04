from setuptools import setup, find_packages

setup(
    name = "LiteroticAPI",
    # major.minor.bugfix
    version = "0.1.1",
    packages = find_packages(),

    # reminder: add BeautifulSoup and requests
    install_requires = ['docutils>=0.3','BeautifulSoup==3','requests'], 

    author = "hrroon",
    description = "an API for Literotica",
    license = "LGPL",
    url = "http://hrroon.github.com/LiteroticAPI"
)
