#!/usr/bin/python
# -*- coding: utf-8 -*-

from cgibase import cgibase
from app_opr.base_opr import basic_opr as db

class Clogin(cgibase):
    def __init__(self):
        return cgibase.__init__(self)

    def onInit(self):
        self.no_check_cookie()  #设置不检查cookies
        if cgibase.pre_do(self):
            opr = self.get_input()
            if opr is None:
                return
            else:
                eval("self.%s()" % opr)
        else:
            return
        self.set_cookies()      #设置cookies


    def login(self):
        try:
            data = self.input["data"]
            user_name = data["user_name"]
            user_psw = data["user_psw"]
            user_info = db().login(user_name)
            userPsw = user_info['password']
            if user_psw != userPsw:
                self.out = '{"status":1, "msg":"密码错误！"}'
            else:
                self.out = '{"status":0, "msg":"登录成功！"}'
        except Exception, e:
            self.out = '{"status":1, "msg":"用户名或者密码错误！"}'

    def logout(self):
        try:
            self.out = '{"status":0, "data":"注销成功"}'
        except Exception, e:
            self.out = '{"status":1, "msg":"'+str(e)+'"}'

if __name__ == "__main__":
    pass
