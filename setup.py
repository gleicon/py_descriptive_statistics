import sys, os, os.path, subprocess
from setuptools.command import easy_install
import pkg_resources as pkgrsrc

from setuptools import setup
from distutils import log
log.set_threshold(log.INFO)

setup(
        name            = "py_descriptive_statistics",
        version         = "0.2",

        packages        = ['py_descriptive_statistics', ],
        zip_safe = False,

        # metadata for upload to PyPI
        author          = "Gleicon Moraes",
        author_email    = "gleicon@gmail.com",
        keywords        = "descriptive statistics enum mean percentile standard deviation variance stats metrics",
        description     = "Descriptive Statistcs for Python - simple library that implements mean, variance, std deviation, percentile over lists of numbers",
        url             =
        "https://github.com/gleicon/py_descriptive_statistics",
    )

