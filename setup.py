import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

import re
versionLine = open("txraft/_version.py", "rt").read()
match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", versionLine, re.M)
versionString = match.group(1)

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        sys.exit(tox.cmdline([]))

setup(name='ctfclient',
      version=versionString,
      description='Raft consensus algorithm for Twisted',
      long_description='An implementation of the Raft distributed consensus '
                       'algorithm, using Twisted.',
      url='https://github.com/lvh/txraft',

      author='Laurens Van Houtven',
      author_email='_@lvh.io',

      packages=["txraft", "txraft.test"],
      test_suite="txraft.test",
      setup_requires=['tox'],
      cmdclass={'test': Tox},
      zip_safe=True,

      license='ISC',
      keywords="twisted raft distributed ha",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Framework :: Twisted",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        ]
)
