#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

from handlers import index, user

url = [
    (r'/', index.IndexHandler),
    (r'/user/(w+)', user.UserHandler)
]