# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'VERSION.txt'), encoding='utf-8') as f:
    version = f.read()

setup(name='morse_game',
      version=version,
      description='A simple little learning tool for learning Morse Code',
      url='https://github.com/zemon1/MorseCodeGame.git',
      author='Jeff Haak',
      author_email='Jeff.Haak@csh.rit.edu',
      license='Apache License 2.0',
      classifiers=[
        'Development Status :: 3 - Alpha',

        'Topic :: Learning Software',

        'License :: OSI Approved :: Apache License 2.0',

        'Programming Language :: Python :: 2.7',
      ],
      keywords='Morse Code Learn Game',
      packages=find_packages(),
      # Include non-python files found in each package in the install.
      include_package_data=True,

      package_data={
        # If any package contains *.json files, include them:
        '': ['*.json'],
      },
      install_requires=[],
      tests_require=['mock'],
      test_suite='tests',

      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[dev,test]
      extras_require={
        'dev': ['mock', 'nose', 'pylint', 'coverage'],
        'rel': ['mock', 'nose', 'pylint', 'coverage', 'bumpversion', 'wheel']
      },

      entry_points={
        'console_scripts': [
            'morseCode=morse_game:morseMain',
        ],
      },
)