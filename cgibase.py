#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, sys
from flask import request
class cgibase:
    def __init__(self):
        self.myinit()

    def __del__(self):
        self.mydel()

    def onInit(self):
        reload(sys)
        sys.setdefaultencoding('utf8')

    def get_input(self):
        a = request.get_data()
        dict1 = json.loads(a)
        return dict1

    def myinit(self):
        self.out = {}
        self.input = {}


    def output(self):
        if type(self.out) is dict:
            return json.dumps(self.out, ensure_ascii=False)
        else:
            return self.out