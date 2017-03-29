#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo

class MongoConn():

    def __init__(self):
        self.client = pymongo.MongoClient('x.x.x.x', 27017)
        self.db = self.client['leason']
        self.connected = self.db.authenticate('leason', 'xxxxx')
