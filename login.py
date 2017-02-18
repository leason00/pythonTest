#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
from flask import request
from cgibase import cgibase

class Clogin(cgibase):
    def __init__(self):
        return cgibase.__init__(self)

    def onInit(self):
        self.out = {}
        opr = self.get_input()["opr"]
        eval("self.%s()" % opr)

    def login(self):
        try:
            data = self.get_input()["data"]
            user_name = data["user"]
            user_psw = data["psw"]
            userPsw = '123456'
            if user_psw != userPsw:
                self.out = '{"status":1, "msg":"密码错误！"}'
            else:
                self.out = '{"status":0, "msg":"登录成功！"}'
        except Exception, e:
            self.out = '{"status":1, "msg":"用户名或者密码错误！"}'

    def logout(self):
        try:
            userinfo = []
            # for user in session.query(User):  # 遍历时查询
            #     idinfo = {"id":str(user.id),"name":str(user.name),"psw":str(user.psw)}
            #     userinfo.append(idinfo)
            # utext = json.dumps(userinfo)
            self.out = '{"status":0, "data":"注销成功"}'
        except Exception, e:
            self.out = '{"status":1, "msg":"'+str(e)+'"}'

if __name__ == "__main__":
    pass