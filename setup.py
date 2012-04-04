from setuptools import setup, find_packages

setup(
    name = "LiteroticAPI",
    version = "0.1.1"
    packages = find_packages(),

    # reminder: add BeautifulSoup and requests
    install_requires = ['docutils>=0.3'], 

    author = "hrroon",
    description = "an API for Literotica",
    license = "LGPL",
    url = "http://hrroon.github.com/LiteroticAPI"
)
