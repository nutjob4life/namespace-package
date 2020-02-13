#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''Testing'''

from codecs import open
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()
with open(path.join(here, 'CHANGES.rst'), encoding='utf-8') as f:
    changes = f.read()


_requirements = [
    'setuptools',  # ALL
    'lxml',
]


setup(
    name='namespace.package',
    version='0.0.0',
    description='Test Package',
    long_description=readme + '\n\n' + changes,
    keywords='test Python Sphinx GitHub actions',
    author='Sean Kelly',
    author_email='kelly@seankelly.biz',
    url='https://github.com/nutjob4life/namespace.package/',
    entry_points={
        'console_scripts': ['heya=namespace.package.main:main']
    },
    namespace_packages=['namespace'],
    packages=find_packages('src', exclude=['docs', 'bootstrap', 'ez_setup']),
    package_dir={'': 'src'},
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst']
    },
    include_package_data=True,
    zip_safe=True,
    install_requires=_requirements,
    extras_require={'test': []},
    license='ALv2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
