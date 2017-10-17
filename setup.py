# -*- coding:utf-8 -*-
#filename:setup

__author__ = 'yibai'
from setuptools import setup, find_packages

setup(
    name = 'yibai-sms-python-sdk',
    version = '1.0.0',
    keywords = ('yibai', 'sdk','python'),
    description = 'yibai-sms-python-sdk',
	license = 'MIT License',
    install_requires = ['requests>=2.9.1'],

    author = 'yibai',
    author_email = 'developer@yibai.com',
    packages = find_packages(),
    platforms = 'any',
)
