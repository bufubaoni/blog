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

with open("config.py", "w") as f:
    f.writelines("""dbconfig = 'mysql://username:password@host/databasename'
    session_option = {
        "session.type": "file",
        # "session.cookie_expires": 30,
        "session.data_dir": "./session",
        "session.auto": True,
        "Session.save_accessed_time": True,
        "Session.timeout": 30
    }""")
