#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from flask import Flask,make_response
from flask import request
from base import *
app = Flask(__name__)
reload(sys)
sys.setdefaultencoding('utf8')

@app.route('/<fun>', methods=['GET', 'POST'])
def index(fun):
    if fun in vpn_index_dict:
        if request.method == 'POST':
            c = vpn_index_dict[fun]
            c.onInit()
            out = c.output()
            resp = make_response(out)
            return resp
        else:
            return '<h1>只接受post请求！</h1>'

@app.route('/user/<name>')
def user(name):
    return'<h1>欢迎, %s</h1>' % name

if __name__ =='__main__':
    app.run(debug=True)