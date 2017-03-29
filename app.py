#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, time, json
from flask import Flask, make_response
from flask import request
from config import cfg
from base import *
app = Flask(__name__)
reload(sys)
sys.setdefaultencoding('utf8')

@app.route('/<fun>', methods=['GET', 'POST'])
def index(fun):
    if fun in post_index_dict:
        if request.method == 'POST':
            c = post_index_dict[fun]
            c.onInit()
            out = c.output()
            print out
            resp = c.make_resp(out)
            return resp
        else:
            return '<h1>只接受post请求！</h1>'
    elif fun in upload_dict:                    #文件上传
        if request.method == "GET":
            return '''
                <!doctype html>
                <title>Upload new File</title>
                <h1>Upload new File</h1>
                <form action="" method=post enctype=multipart/form-data>
                  <p><input type=file name=file>
                     <input type=submit value=Upload>
                </form>
                '''
        elif request.method == "POST":
            c = upload_dict[fun]
            c.onInit()
            out = json.loads(c.output())
            file = request.files['file']
            filename = file.filename
            print filename
            if '.' in filename and filename.rsplit('.', 1)[1] in out["allow"]:
                f = "%.20f" % time.time()
                f += ".png"
                file.save(out["path"] + f)
                pic_url = out["path"] + f
                out = {"status": 0, "pic_url": pic_url}
                return json.dumps(out, ensure_ascii=False)
    else:
        return make_response(cfg.err['refused'])

@app.route('/user/<name>')
def user(name):
    return'<h1>欢迎, %s</h1>' % name

if __name__ =='__main__':
    app.run(debug=True)