#!/usr/bin/env python
# -*- coding: utf-8 -*-
# just is a simple app
from bottle import route, run
from model import db_shadowsocks
import json

@route('/')
def index():
    return "this is index for roote"

@route("/userlist")
def userlist():
    userlist=db_shadowsocks(db_shadowsocks.user.id>0).select()
    
    return json.dumps(userlist.as_dict())

@route("/adduser")
def adduser():
    return "this is add user"

@route("/userinfo/<userid:int>")
def userinf(userid):
    if userid:
        return "user id is {id}".format(id=userid)

@route("/userdelete/<userid:int>")
def deleteuser(userid):
    if userid:
        return "seccuss delete user id is {id}".format(id=userid)


run(host='localhost', port=8000, debug=True)
