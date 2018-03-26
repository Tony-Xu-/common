# coding=utf-8
"""
Usage:

from mysqlkeeper import *
sql_cmd = 'SELECT * FROM table WHERE k = v'
results = MysqlKeeper().select_db(sql_cmd)
"""
import MySQLdb
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import config

conn = None
v = config.get_conf()
# print v

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MysqlKeeper(Singleton):
    def __init__(self):
        self.mysql_server = v["mysql"]['host']
        self.mysql_port = v["mysql"]['port']
        self.user = v["mysql"]['username']
        self.password = v["mysql"]['password']
        self.database = v["mysql"]['db']
        global conn
        if not conn or not conn.open:
            conn = MySQLdb.connect(host=self.mysql_server, port=self.mysql_port, user=self.user, passwd=self.password)
            conn.select_db(self.database)
    
    def get_db_conn(self):
        global conn
        if conn:
            return conn
        else:
            conn = MySQLdb.connect(host=self.mysql_server, port=self.mysql_port, user=self.user, passwd=self.password)
            conn.select_db(self.database)
    
    def update_db(self, sql):
        global conn
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    
    def update_db_ext(self, sql, data):
        global conn
        c = conn.cursor()
        c.execute(sql, data)
        conn.commit()
    
    def select_db(self, sql):
        global conn
        c = conn.cursor()
        # print sql
        c.execute(sql)
        return c.fetchall()
    
    def select_db_ext(self, sql, data):
        global conn
        c = conn.cursor()
        c.execute(sql, data)
        return c.fetchall()
    
    def __del__(self):
        if conn:
            conn.close()
