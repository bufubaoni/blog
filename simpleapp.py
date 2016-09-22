#!/usr/bin/env python
# -*- coding: utf-8 -*-
# just is a simple app
from bottle import route, run, request, post
from model import db_shadowsocks
from beaker.middleware import SessionMiddleware
import bottle
import json
from config import session_option
from Auth import RequireLoginLogin,RequireAuth
app = bottle.app()
myapp = SessionMiddleware(app, session_option)


@route('/')
@RequireLoginLogin
def index():
    return "it is index "


@route("/listuser")
def userlist():
    userlist = db_shadowsocks(db_shadowsocks.user.id > 0).select(db_shadowsocks.user.id,
                                                                 db_shadowsocks.user.email,
                                                                 db_shadowsocks.user.port, )
    return json.dumps(userlist.as_dict())


@route("/adduser")
@post("/adduser")
@RequireAuth("admin")
def adduser():
    if request.method == "POST":
        return request.body
    return "you can add user in this fun"


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


@route("/autherror")
def autherror():
    return "auth error you get"

bottle.run(app=myapp, host='localhost', port=8000,debug=True )
