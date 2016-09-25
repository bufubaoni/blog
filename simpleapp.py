#!/usr/bin/env python
# -*- coding: utf-8 -*-
# just is a simple app
from bottle import route, request, post, json_dumps, json_lds, error
from model import db_shadowsocks, db_add, db_delet
from beaker.middleware import SessionMiddleware
import bottle
from config import session_option
from Auth import RequireLogin, RequireAuth, setSession
from Form import Form
import User

app = bottle.app()
myapp = SessionMiddleware(app, session_option)


@route('/')
@setSession
def index(session=None):
    if session.get("username"):
        return "user: {username}".format(username=session["username"])
    return "it is index "


@route("/listuser")
def userlist():
    users = db_shadowsocks(db_shadowsocks.user.id > 0).select(db_shadowsocks.user.id,
                                                              db_shadowsocks.user.email,
                                                              db_shadowsocks.user.port,
                                                              db_shadowsocks.user.type)
    return json_dumps(users.as_dict())


@route("/adduser")
@post("/adduser")
@RequireAuth("admin")
def adduser(session=None):
    if request.method == "POST":
        try:
            newuser = json_lds(request.body)
        except TypeError:
            newuser = {key: value[0] for key, value in request.forms.dict.items()}
        if newuser:
            return json_dumps(db_add(newuser))
    return Form("/adduser", *["email",
                              "passwordforss",
                              "passwd",
                              "d",
                              "u",
                              "transfer_enable",
                              "switch",
                              "enable", ]).form()


@route("/infouser")
@RequireLogin
def userinfo(session=None):
    userid = session.get("id")
    if userid:
        user = db_shadowsocks(db_shadowsocks.user.id == userid).select().first()
        return json_dumps(user.as_dict())
    return "some user info but you didn't input anything"


@route("/deleteuser")
@route("/deleteuser/<userid:int>")
@RequireAuth("admin")
def deleteuser(session=None, userid=None):
    if userid:
        return json_dumps(db_delet(userid))


@route("/edituser")
@route("/edituser/<userid:int>")
@post("/edituser/<userid:int>")
@RequireAuth("admin")
def edituser(session=None, userid=None):
    if request.method == "GET" and userid:
        user = db_shadowsocks(db_shadowsocks.user.id == userid).select(
            db_shadowsocks.user.transfer_enable,
            db_shadowsocks.user.port,
            db_shadowsocks.user.switch,
            db_shadowsocks.user.enable
        ).first()
        return Form("/edituser/{userid}".format(userid=userid), **user.as_dict()).form()
    elif request.method == "POST" and userid:
        try:
            info = json_lds(request.body)
        except TypeError as e:
            info = {key: value[0] for key, value in request.forms.dict.items()}
        try:
            db_shadowsocks(db_shadowsocks.user.id == userid).update(**info)
        except Exception as e:
            return e
        finally:
            db_shadowsocks.commit()
        return "edit user seccuss"

    return "edit user for admin"


@error(403)
@route("/autherror")
def autherror():
    return "auth error you get"


bottle.run(app=myapp, host='localhost', port=8000, debug=True)
