# -*- coding:UTF-8 -*-
from configparser import ConfigParser


class ConfigIni(object):
    def __init__(self,inifile):
        self.inifile = inifile
        self.cfg = ConfigParser()
        self.cfg_load()

    # 加载配置文件
    def cfg_load(self):
        self.cfg.read(self.inifile,"utf-8")

    # 打印出所有配置
    def cfg_dump(self):
        sessions = self.cfg.sections()
        for session in sessions:
            print(session)
            print(self.cfg.items(session))

    # 删除一个session的条目
    def delete_item(self,session,key):
        self.cfg.remove_option(session,key)

    # 删除一个session
    def delete_session(self,session):
        self.cfg.remove_section(session)

    # 需改或添加一个session条目
    def set_item(self,session, key, value):
        self.cfg.set(session, key, value)

    # 添加一个session
    def add_session(self,session):
        self.cfg.add_section(session)

    # 获取session中的条目
    def getItems(self,session):
        return self.cfg.items(session)

    # 获取所有的session
    def getSessions(self):
        return self.cfg.sections()

    # 保存配置
    def save(self):
        file = open(self.inifile,"w")
        self.cfg.write(file)
        file.close()
