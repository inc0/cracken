# -*- encoding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages

assert sys.version_info >= (2, 7), "Python 2.7+ required."

current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, 'README.md')) as readme_file:
        long_description = readme_file.read()

setup(
    name='cracken',
    version='0.0.1',
    author='Contributors',
    author_email='inc007@gmail.com',
    description="Cool voice changer with magick and cookies",
    long_description=long_description,
    keywords='',
    platforms=['any'],
    license='Apache Software License v2.0',
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    zip_safe=False,  # because templates are loaded from file path
    install_requires=[
        'numpy',
        'pyaudio',
    ],
    entry_points={
        'console_scripts': [
            'cracken = cracken.main:run',
        ],
    },
)
