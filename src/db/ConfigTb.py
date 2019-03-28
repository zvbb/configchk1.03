# -*- coding:UTF-8 -*-

import pymysql

class ConfigTb(object):
    def __init__(self,conn):
        self.conn = conn
        self.rows = {}
        self.loadConfigTb()

    def loadConfigTb(self):
        sql = "select * from qconfig;"

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.conn.cursor()

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)

        for row in cursor.fetchall():
            self.rows[row[0]] = row

        # 关闭数据库连接
        self.conn.close()

    def getRow(self,configName):
        return self.rows[configName]