#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Form(object):
    def __init__(self, url, *args):
        self._url = url
        self._para = args

    def form(self):
        inputs = "</br>".join(map(self.input, self._para))
        return ("<form action='{action}' method='post'>"
                "{inputs}"
                "</br>"
                "{submit}"
                "</form>".format(action=self._url, inputs=inputs, submit=self.submit()))

    def input(self, name):
        return ("<input type='text' placeholder={name} name={name}>".format(name=name))

    def submit(self):
        return ("<input type='submit' value='submit'/> "
                "<input type='button' value='cancel'>")
