#!/usr/bin/python
# -*- coding: utf-8 -*-

from db_conn.cont_mongo import MongoConn

class basic_opr():
    def __init__(self):
        self.db = MongoConn().db

    def login(self, user_name):
        userInfo = self.db['test'].find_one({'_id': user_name})
        return userInfo

if __name__ == "__main__":
    pass
    # aaa = basic_opr()
    # aaa.login('leason')