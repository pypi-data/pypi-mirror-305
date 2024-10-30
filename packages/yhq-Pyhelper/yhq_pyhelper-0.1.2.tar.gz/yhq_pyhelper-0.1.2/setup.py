#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : HuiQing Yu
# @Date   : 2024/10/30
# @Description:

from setuptools import setup, find_packages

setup(
    name='yhq-Pyhelper',
    version='0.1.2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pymysql==1.1.0',
        'allure-pytest==2.13.2',
        'requests==2.31.0',
    ],
    author='Yu HuiQing',
    author_email='yuhuiqing@aliyun.com',
    description='A brief description of the package.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HuiQingGit/yhq-Pyhelper.git',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    include_package_data=True,
    zip_safe=False,
)
