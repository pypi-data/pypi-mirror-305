#!/usr/bin/env python
# encoding=utf-8
# maintainer: Yasusync

from __future__ import absolute_import
from __future__ import unicode_literals
import setuptools

setuptools.setup(
    name='ethio-date-converter',  # Package name
    version='0.1.5',  # Version of your package
    license='GNU General Public License (GPL), Version 3',  # License type

    provides=['ethiopian_date'],  # Specify the modules provided

    description='Ethiopian date converter.',  # Short description
    long_description=open('README.md').read(),  # Long description read from README
    long_description_content_type='text/markdown',  # Specify content type as Markdown
    url='https://github.com/Yasusync/ethiopian_date_converter',  # Your project URL

    packages=setuptools.find_packages(),  # Automatically find packages

    install_requires=[  # Dependencies
        'six>=1.11.0',
    ],

    classifiers=[  # Metadata for PyPI
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
    ],
)
