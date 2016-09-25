# simple ss manyuser panel for person
just admin something
if you want run it 
your should creat /config.py that content
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    dbconfig = 'mysql://username:password@host/databasename'
    session_option = {
        "session.type": "file",
        "session.cookie_expires": 300,
        "session.data_dir": "./session",
        "session.auto": True,
        "Session.save_accessed_time": True,
    }

the app use third libs

    pyDAL
    beaker
    bottle

db driver is :

    pymysql

you should install all requires