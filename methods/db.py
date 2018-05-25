#!/usr/bin/env Python
# coding=utf-8

import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="12345678", db="qiwsirtest", port=3306, charset="utf8")
cur = conn.cursor()