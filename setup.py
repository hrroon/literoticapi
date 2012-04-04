from setuptools import setup, find_packages

setup(
    name = "LiteroticAPI",
    # major.minor.bugfix
    version = "0.1.1",
    packages = find_packages(),

    # reminder: add BeautifulSoup and requests
    install_requires = [
        'BeautifulSoup < 4',
        'requests',
        'gevent',
    ], 

    author = "hrroon",
    description = "an API for Literotica",
    long_description = open("README").read(),
    license = "LGPL",
    url = "http://hrroon.github.com/LiteroticAPI",
)
