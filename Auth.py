#!/usr/bin/env python
# -*- coding: utf-8 -*-
from emu_auth import emu_auth_type
from bottle import request, redirect


def RequireLoginLogin(action):
    def login(*args, **kwargs):
        session = request.environ.get("beaker.session")
        print(session)
        if session.get("email"):
            print ("must")
            return action(*args, **kwargs)
        else:
            redirect("/autherror")

    return login


def RequireAuth(authname):
    def auth(action):
        def conaction(*args, **kwargs):
            session = request.environ.get("beaker.session")
            if session.get("usertype") and \
                            session.get("usertype") == emu_auth_type(authname):
                return action(*args, **kwargs)
            else:
                redirect("/autherror")
        return conaction
    return auth
