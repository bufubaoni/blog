#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Form(object):
    def __init__(self, url, *args, **kwargs):
        self._url = url
        self._para = args
        self._kwargs = kwargs

    def form(self):
        if self._para:
            inputs = "</br>".join(map(self.input, self._para))
        else:
            inputs = "</br>".join([self.input_v(k, v) for k, v in self._kwargs.items()])
        return ("<form action='{action}' method='post'>"
                "{inputs}"
                "</br>"
                "{submit}"
                "</form>".format(action=self._url, inputs=inputs, submit=self.submit()))

    def input(self, name):
        return ("<input type='text' placeholder={name} name={name} />".format(name=name))

    def input_v(self, name, value):
        return ("<input type='text' placeholder={name} name={name} value={value} />"
                "".format(name=name, value=str(value)))

    def submit(self):
        return ("<input type='submit' value='submit'/> "
                "<input type='button' value='cancel'>")


if __name__ == "__main__":
    print (Form("/test", **{"id": 1, "test": "test"}).form())
