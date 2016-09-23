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
    userlist=db_shadowsocks(db_shadowsocks.user.id>0).select(
                                                            db_shadowsocks.user.id,
                                                            db_shadowsocks.user.email,
                                                            db_shadowsocks.user.port,)
    return json.dumps(userlist.as_dict())

@route("/adduser")
def adduser():
    return "this is add user"

@route("/userinfo/<userid:int>")
def userinfo(userid):
    if userid:
        userinfo=db_shadowsocks(db_shadowsocks.user.id==userid).select().first()
        return json.dumps(userinfo.as_dict())

@route("/userdelete/<userid:int>")
def deleteuser(userid):
    if userid:
        return "seccuss delete user id is {id}".format(id=userid)


run(host='localhost', port=8000, debug=True)
