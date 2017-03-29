#!/usr/bin/python
# -*- coding: utf-8 -*-

from cgibase import cgibase

class Cupload(cgibase):
    def __init__(self):
        return cgibase.__init__(self)

    def onInit(self):
        self.no_check_cookie()  #设置不检查cookies
        if cgibase.pre_do(self):
            opr = 'upload'
            if opr is None:
                return
            else:
                eval("self.%s()" % opr)
        else:
            return
        # self.set_cookies()  # 设置cookies

    def allow_ext(self):
        return ["jpg", "png"]

    def get_tmp_path(self):
        return "/www/80/pic/"

    def upload(self):
        self.out = {"status": 0, "allow": ["jpg","png"], "path": "img/"}



if __name__ == "__main__":
    pass