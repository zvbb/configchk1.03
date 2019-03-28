import re


class CheckConfig(object):
    CheckFail = []

    def __init__(self,configIni,configTb,gsLog):
        self.configIni = configIni
        self.configTb = configTb
        self.gsLog = gsLog

    def check_row(self,rowName):
        items = self.configIni.getItems(rowName)
        if(items == None):
            return True
        cols = self.configTb.getRow(rowName)

        tmp = [1,1,1,1,1]
        for item in items:
            if(item[0]=="datatype"):
                tmp[0] = item[1]

            if(item[0]=="limit"):
                tmp[1] = item[1]

            if(item[0]=="split"):
                tmp[2] = item[1]

            if (item[0] == "splitstep0"):
                tmp[3] = item[1]

            if (item[0] == "splitstep1"):
                tmp[4] = item[1]

        if(tmp[0]=="int"):
            try:
                val = int(cols[1])
                return
            except Exception as e:
                self.gsLog.info(rowName + " row is config error ...")
                CheckConfig.CheckFail.append(rowName)
                return

        if (tmp[0] == "string"):
            try:
                val = cols[2]
                # 如果该项没有填值
                if(val==""):
                    return

                splits = tmp[2]
                if(splits==""):
                    if(tmp[1]=="bool"):
                        if(self.is_bool(val) == False):
                            self.gsLog.info(rowName + " row is config error ...")
                            CheckConfig.CheckFail.append(rowName)
                            return

                    if(tmp[1]=="ip"):
                        if(self.is_ip(val) == False):
                            self.gsLog.info(rowName + " row is config error ...")
                            CheckConfig.CheckFail.append(rowName)
                            return

                # 指定字符分割配置
                else:
                    split_len = len(splits)
                    valStep0 = []
                    valStep1 = []
                    if(split_len==1):
                        valStep0 = val.split(splits)
                        for step0 in valStep0:
                            if(tmp[3] == "string"):
                                return

                            if (tmp[3] == "bool"):
                                if (self.is_bool(step0) == False):
                                    self.gsLog.info(rowName + " row is config error ...")
                                    CheckConfig.CheckFail.append(rowName)
                                    return

                            if (tmp[3] == "ip"):
                                if (self.is_ip(step0) == False):
                                    self.gsLog.info(rowName + " row is config error ...")
                                    CheckConfig.CheckFail.append(rowName)
                                    return

                            if (tmp[3] == "int"):
                                if(self.is_num(step0) == False):
                                    self.gsLog.info(rowName + " row is config error ...")
                                    CheckConfig.CheckFail.append(rowName)
                                    return

                    if(split_len==2):
                        valTmp = val.split(splits[0])
                        for it in valTmp:
                            tmp1 = it.split(splits[1])
                            if(len(tmp1)==2):
                                valStep0.append(tmp1[0])
                                valStep1.append(tmp1[1])

                        for step0 in valStep0:
                            if (tmp[3] == "string"):
                                return

                            if (tmp[3] == "bool"):
                                if (self.is_bool(step0) == False):
                                    self.gsLog.info(rowName + " row is config error ...")
                                    CheckConfig.CheckFail.append(rowName)
                                    return

                            if (tmp[3] == "ip"):
                                if (self.is_ip(step0) == False):
                                    self.gsLog.info(rowName + " row is config error ...")
                                    CheckConfig.CheckFail.append(rowName)
                                    return

                            if (tmp[3] == "int"):
                                if (self.is_num(step0) == False):
                                    self.gsLog.info(rowName + " row is config error ...")
                                    CheckConfig.CheckFail.append(rowName)
                                    return


                        for step1 in valStep1:
                            if (tmp[4] == "string"):
                                return

                            if (tmp[4] == "bool"):
                                if (self.is_bool(step1) == False):
                                    self.gsLog.info(rowName + " row is config error ...")
                                    CheckConfig.CheckFail.append(rowName)
                                    return

                            if (tmp[4] == "ip"):
                                if (self.is_ip(step1) == False):
                                    self.gsLog.info(rowName + " row is config error ...")
                                    CheckConfig.CheckFail.append(rowName)
                                    return

                            if (tmp[4] == "int"):
                                if (self.is_num(step1) == False):
                                    self.gsLog.info(rowName + " row is config error ...")
                                    CheckConfig.CheckFail.append(rowName)
                                    return
            except Exception as e:
                self.gsLog.info(rowName + " row is config error ...")
                CheckConfig.CheckFail.append(rowName)
                return

    def check_all(self):
        sessions = self.configIni.getSessions()
        for session in sessions:
            if(self.check_row(session)):
                CheckConfig.CheckFail.append(session)

    # str是数字
    def is_num(self,str):
        try:
            tmp = int(str)
            return True
        except Exception as e:
            return False

    # str是bool类型
    def is_bool(self,str):
        if (str != "false" and str != "true"):
            return False
        return True

    # 精确的匹配给定的字符串是否是IP地址
    def is_ip(self,str):
        if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",str):
            return True
        else:
            return False
