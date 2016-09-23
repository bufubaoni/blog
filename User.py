#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, post, request, redirect


@route("/login")
@post("/login")
def login():
    if request.method == "POST":
        username = request.forms["username"]
        # password = request.forms["password"]
        session = request.environ.get("beaker.session")
        session["username"] = username
        redirect("/")
    return "<form action='/login' method='post'><input name='username' /></br><input type='submit'></form>"


