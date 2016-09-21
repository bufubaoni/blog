#!/usr/bin/env python
# -*- coding: utf-8 -*-
# just is a simple app
from bottle import route, run


@route('/')
def index():
    return "this is index for roote"

@route("/userlist")
def userlist():
    return "this is user list"

@route("/adduser")
def adduser():
    return "this is add user"

@route("/userinfo/<userid:int>")
def userinf(userid):
    if userid:
        return "user id is {id}".format(id=userid)


run(host='localhost', port=8000, debug=True)
