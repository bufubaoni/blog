#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, post, request, redirect,json_lds,json_dumps
from model import db_shadowsocks
from Auth import RequireLogin


@route("/login")
@post("/login")
def login():
    if request.method == "POST":
        username = request.forms["username"]
        password = request.forms["password"]
        user = {key: value[0] for key, value in request.forms.dict.items()}
        return json_dumps(user)
        # users = db_shadowsocks((db_shadowsocks.user.email == username.strip()) &
        #                        (db_shadowsocks.user.passwd == password.strip()))
        # user = users.select().first()
        # if user:
        #     session = request.environ.get("beaker.session")
        #     session["username"] = username
        #     session["type"] = user.type
        #     session["id"] = user.id
        #     session["userid"] = user.id
        #     session["email"] = username
        #     redirect("/")
    return "<form action='/login' method='post'>" \
           "<input name='username' />" \
           "</br>" \
           "<input name='password' type='password'>" \
           "</br>" \
           "<input type='submit'></form>"
@route("/logout")
@RequireLogin
def logout(session=None):
    if session:
        session.delete()
    return "logout seccuss"
