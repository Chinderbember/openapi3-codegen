#!/usr/bin/env python

from os.path import dirname, join

from iniconfig import IniConfig
from setuptools import find_packages, setup

from src import codegen

description_file = join(dirname(__file__), "readme.md")
packages = list(IniConfig("Pipfile").sections['packages'].keys())

setup(
    name=codegen.__title__,
    author=codegen.__author__,
    author_email=codegen.__email__,
    url="https://github.com/manchenkoff/openapi3-codegen",
    project_urls={
        "Source": "https://github.com/manchenkoff/openapi3-codegen",
    },
    version=codegen.__version__,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    license="MIT",
    description=codegen.__description__,
    long_description=open(description_file).read(),
    long_description_content_type="text/markdown",
    keywords="swagger, python, code-generation, code-generator, codegen, openapi3, swagger-api",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=packages,
    entry_points={
        'console_scripts': [
            'openapi3-codegen=codegen.__main__:run'
        ]
    }
)
