#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

# prevent unnecessary installation of pytest-runner
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(name="doctest",
      description="doctest description",
      version=1.0,
      author="Aditya Dange",
      author_email="adityadange.ska@gmail.com",
      license="BSD3",
      packages=find_packages(),
      include_package_data=True,
      url='https://www.skatelescope.org/',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: Other/Proprietary License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Scientific/Engineering :: Astronomy"],
      platforms=["OS Independent"],
      setup_requires=[] + pytest_runner,
      install_requires=[
          "enum34",
          "argparse",
          "future"
      ],
      tests_require=[
          "coverage",
          "pytest",
          "pytest-cov",
          "pytest-xdist"
      ],
      keywords="doctest readthedocs sphinx",
      zip_safe=False)
