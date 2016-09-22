#!/usr/bin/env python
# -*- coding: utf-8 -*-
# just is a simple app
from bottle import route, run, request, post
from model import db_shadowsocks
import json


@route('/')
def index():
    return "this is index for roote"


@route("/listuser")
def userlist():
    userlist = db_shadowsocks(db_shadowsocks.user.id > 0).select(db_shadowsocks.user.id,
                                                                 db_shadowsocks.user.email,
                                                                 db_shadowsocks.user.port, )
    return json.dumps(userlist.as_dict())


@route("/adduser")
@post("/adduser")
def adduser():
    user = request.body
    return user


@route("/infouser")
@route("/infouser/<userid:int>")
def userinfo(userid=None):
    if userid:
        userinfo = db_shadowsocks(db_shadowsocks.user.id == userid).select().first()
        return json.dumps(userinfo.as_dict())
    return "some user info but you didn't input anything"


@route("/deleteuser")
@route("/deleteuser/<userid:int>")
def deleteuser(userid=None):
    if userid:
        return "seccuss delete user id is {id}".format(id=userid)


run(host='localhost', port=8000, debug=True)
