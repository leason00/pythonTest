#!/usr/bin/python
# -*- coding: utf-8 -*-

cookies_name = 'ssid'

err = {
    "refused":'{"status":1, "msg":"拒绝访问！"}',
    "input_err":'{"status":2, "msg":"输入错误！"}',
    "relogin":'{"status":3, "msg":"会话超时，需要重新登录！", "need_login":1}',
}