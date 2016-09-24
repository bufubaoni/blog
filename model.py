#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydal import DAL, Field
from config import dbconfig

db_shadowsocks = DAL(dbconfig)
db_shadowsocks.define_table("user",
                            Field("id", "id"),
                            Field("email", "string"),
                            Field("passwordforss", "string", rname="pass"),
                            Field("passwd", "string"),
                            Field("t", "integer"),
                            Field("u", "bigint"),
                            Field("d", "bigint"),
                            Field("transfer_enable", "bigint"),
                            Field("port", "integer"),
                            Field("switch", "integer"),
                            Field("enable", "integer"),
                            Field("type", "integer"),
                            Field("last_get_gift_time", "integer"),
                            Field("last_rest_pass_time", "integer"),
                            migrate=False)


def db_add(user):
    last_id = db_shadowsocks(db_shadowsocks.user.id > 0). \
        select(db_shadowsocks.user.id).last()
    user.update({"id": last_id + 1})
    try:
        userid = db_shadowsocks.user.insert(**user)
    except Exception as e:
        return (False, "fault by " + e.message)
    finally:
        db_shadowsocks.commit()
    return (True, "insert user id is {id}".format(id=userid))
