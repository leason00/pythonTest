#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

RANDON_CHAR = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

def randomStr(randomlength=128):
    str = ''
    chars = RANDON_CHAR
    length = len(chars) - 1
    for i in range(randomlength):
        str += chars[ord(os.urandom(1)) % length]
    return str