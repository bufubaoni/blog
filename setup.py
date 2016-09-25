#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="simple_app",
    version="1.0",
    install_requires=[
        "pyDAL",
        "pymysql",
        "beaker"
    ],
)