#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    "Pydantic",
    "PyYAML",
    "Rich",
    "singleton-decorator",
]

test_requirements = [ ]

setup(
    author="Jaideep Sundaram",
    author_email='sundaram.baylorgenetics@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Collection of Python modules for managing controlled vocabularies.",
    entry_points={},
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bg_controlled_vocabularies_utils',
    name='bg_controlled_vocabularies_utils',
    packages=find_packages(include=['bg_controlled_vocabularies_utils', 'bg_controlled_vocabularies_utils.*']),
    package_data={"bg_controlled_vocabularies_utils": ["conf/config.yaml"]},
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rusty-bioinfo-se/bg-controlled-vocabularies-utils',
    version='0.1.0',
    zip_safe=False,
)
