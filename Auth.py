#!/usr/bin/env python
# -*- coding: utf-8 -*-
from emu_auth import emu_auth_type
from bottle import request, redirect


def setSession(action):
    def sessions(*args, **kwargs):
        session = request.environ.get("beaker.session")
        return action(session=session, *args, **kwargs)
    return sessions


def RequireLogin(action):
    def login(*args, **kwargs):
        session = request.environ.get("beaker.session")
        if session.get("email"):
            return action(session=session, *args, **kwargs)
        else:
            redirect("/autherror")

    return login


def RequireAuth(authname):
    def auth(action):
        def conaction(*args, **kwargs):
            session = request.environ.get("beaker.session")
            if session.get("usertype") == emu_auth_type[authname]:
                return action(session=session, *args, **kwargs)
            else:
                redirect("/autherror")
        return conaction
    return auth
