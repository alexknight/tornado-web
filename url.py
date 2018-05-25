#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

from handlers import index, user, sleep

url = [
    (r'/', index.IndexHandler),
    (r'/user', user.UserHandler),
    (r'/sleep', sleep.SleepHandler)
]