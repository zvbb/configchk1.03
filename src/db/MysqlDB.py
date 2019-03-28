from configparser import ConfigParser

import logging
import pymysql


class MysqlDB(object):
    def __init__(self,configFile):
        self.configFile = configFile
        self.host = None
        self.user = None
        self.passwd = None
        self.database = None
        self.port = None
        self.initConfig()

    def initConfig(self):
        try:
            logConfig = ConfigParser()
            logConfig.read(self.configFile)
            for session in logConfig.sections():
                if(session == "mysql"):
                    items = logConfig.items(session)
                    for item in items:
                        if(item[0]=="user".lower()):
                            self.user = item[1]

                        if(item[0]=="passwd".lower()):
                            self.passwd = item[1]

                        if (item[0] == "port".lower()):
                            self.port = int(item[1])

                        if (item[0] == "host".lower()):
                            self.ip = item[1]

                        if (item[0] == "database".lower()):
                            self.database = item[1]
        except Exception as e:
            logging.error(e)

    def getConnect(self):
        # 打开数据库连接
        conn = pymysql.connect(self.host, self.user, self.passwd,self.database,self.port)
        return conn
