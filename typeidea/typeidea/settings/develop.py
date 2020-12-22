# -*- coding:utf8 -*-
'''
@author: zhubo
@email: bo.zhu@crgecent.com
@file: develop.py
@time: 2020/12/22 17:38
@desc:
'''


from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}