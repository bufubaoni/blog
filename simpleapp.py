#!/usr/bin/env python
# -*- coding: utf-8 -*-
# just is a simple app
from bottle import route, run, request, post
from model import db_shadowsocks
from beaker.middleware import SessionMiddleware
import bottle
import json
from config import session_option
from Auth import RequireLogin, RequireAuth, setSession
import User

app = bottle.app()
myapp = SessionMiddleware(app, session_option)


@route('/')
@setSession
def index(session=None):
    # session = request.environ.get("beaker.session")
    if session.get("username"):
        return "user: {username}".format(username=session["username"])
    return "it is index "


@route("/listuser")
def userlist():
    users = db_shadowsocks(db_shadowsocks.user.id > 0).select(db_shadowsocks.user.id,
                                                              db_shadowsocks.user.email,
                                                              db_shadowsocks.user.port,
                                                              db_shadowsocks.user.type)
    return json.dumps(users.as_dict())


@route("/adduser")
@post("/adduser")
@RequireAuth("admin")
def adduser(session=None):
    if request.method == "POST":
        return request.body
    return "you can add user in this fun"


@route("/infouser")
@RequireLogin
def userinfo(session=None):
    userid = session.get("id")
    if userid:
        user = db_shadowsocks(db_shadowsocks.user.id == userid).select().first()
        return json.dumps(user.as_dict())
    return "some user info but you didn't input anything"


@route("/deleteuser")
@route("/deleteuser/<userid:int>")
@RequireAuth("admin")
def deleteuser(session=None, userid=None):
    if userid:
        return "seccuss delete user id is {id}".format(id=userid)


@route("/autherror")
def autherror():
    return "auth error you get"


bottle.run(app=myapp, host='localhost', port=8000, debug=True)
