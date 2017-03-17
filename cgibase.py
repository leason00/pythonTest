#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, sys
from flask import request
from flask import make_response
from config import cfg
from lib.lib_util import randomStr

class cgibase:
    def __init__(self):
        self.myinit()

    def __del__(self):
        pass

    def pre_do(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        if self.__checkCookieFlag == False:
            return True
        else:
            if self.check_cookie():
                return True
            else:
                return False

    def get_input(self):
        a = request.get_data()
        try:
            dict = json.loads(a)
            opr = dict["opr"]
            self.input = dict
        except:
            opr = None
            self.out = cfg.err['input_err']
        return opr

    def myinit(self):
        self.out = {}
        self.input = {}
        self.__setCookieFlag = False
        self.__checkCookieFlag = True


    def output(self):
        if type(self.out) is dict:
            return json.dumps(self.out, ensure_ascii=False)
        else:
            return self.out

    def make_resp(self, data):
        resp = make_response(data)
        if self.__setCookieFlag:
            resp.set_cookie(cfg.cookies_name, randomStr())
        return resp

    def set_cookies(self):
        self.__setCookieFlag = True
        return

    def no_check_cookie(self):
        self.__checkCookieFlag = False
        return

    def check_cookie(self):
        sid = request.cookies.get('ssid')
        print sid
        if sid == '' or sid is None:
            self.out = cfg.err['relogin']
            return False
        return True


if __name__ == "__main__":
    pass