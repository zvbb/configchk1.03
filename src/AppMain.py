import sys

from check.CheckConfig import CheckConfig
from check.ConfigIni import ConfigIni
from db.ConfigTb import ConfigTb
from db.MysqlDB import MysqlDB
from log.Log import *

gsLog = None

if __name__ == '__main__':
    if(len(sys.argv)>1):
        if(sys.argv[1] == "check"):
            configFile = "../config/project.ini"
            configIniFile = "../config/config.ini"
            # 初始化全局Log对象
            gsLog = Log(configFile).getLog()
            gsLog.info("start check config table ...")

            # 获取数据库连接
            gsLog.info("get connection ...")
            mysqldb = MysqlDB(configFile)
            conn = mysqldb.getConnect()

            # 获取config表数据
            gsLog.info("get qconfig data ...")
            configTb = ConfigTb(conn)

            # 加载对config表中字段 应该符合的标准
            gsLog.info("load config.ini ...")
            configIni = ConfigIni(configIniFile)

            # 开始检查qconfig表中的配置
            gsLog.info("start check ...")
            checkConfig = CheckConfig(configIni,configTb,gsLog)
            checkConfig.check_all()


            # 总结检查结果
            gsLog.info("summary ===>> : error config row are :"+CheckConfig.CheckFail.__str__())







