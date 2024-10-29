#! /usr/bin/env python

from setuptools import setup, find_packages, Command

from distutils.command.build_py import build_py

setup(
    name             = 'SaintGSE',
    version          = '0.5.1',
    description      = 'Package for distribution',
    author           = 'msjeon27',
    author_email     = 'msjeon27@naver.com',
    url              = 'https://github.com/MSjeon27/SaintGSE',
    download_url     = '',
    install_requires = ['torch', 'pandas', 'numpy', 'sklearn'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['SAINTGSE', 'SaintGSE'],
    cmdclass         = {'build_py': build_py},
    python_requires  = '>=3.8',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ]
) 
