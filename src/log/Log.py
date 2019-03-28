# -*- coding: utf-8 -*-
import logging
import logging.handlers
import datetime
import sys
from configparser import ConfigParser


class Log(object):
    def __init__(self,configFile):
        # log的配置文件
        self.configFile = configFile
        # log的输出级别
        self.level = None
        # log的输出位置
        self.logFile = None
        self.initConfig()

    def getLog(self):
        logger = logging.getLogger('configchk')
        logger.setLevel(int(self.level))
        # 设置Handler,输出到指定文件
        rf_handler = logging.handlers.TimedRotatingFileHandler(self.logFile, when='midnight', interval=1, backupCount=7)
        rf_handler.setFormatter(logging.Formatter("%(asctime)s- %(levelname)s - %(pathname)s - %(funcName)s(%(lineno)d) : %(message)s"))

        # 打印大控制台的Handler
        f_handler = logging.StreamHandler(sys.stdout)
        f_handler.setLevel(int(self.level))
        f_handler.setFormatter(logging.Formatter("%(asctime)s- %(levelname)s - %(pathname)s - %(funcName)s(%(lineno)d) : %(message)s"))

        #logger添加Handler
        logger.addHandler(rf_handler)
        logger.addHandler(f_handler)

        return logger

    def initConfig(self):
        try:
            logConfig = ConfigParser()
            logConfig.read(self.configFile)
            for session in logConfig.sections():
                if(session == "log"):
                    items = logConfig.items(session)
                    for item in items:
                        if(item[0]=="level"):
                            self.level = item[1]

                        if(item[0]=="logFile".lower()):
                            self.logFile = item[1]
        except Exception as e:
            logging.error(e)

