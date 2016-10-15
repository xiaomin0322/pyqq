# -*- coding: utf8 -*-
class dt:   # datatype  数据类型
    def __init__(self):
        class qq_info():
            def __init__(self):
                self.Account = ""    # qq
                self.QQ = 0    # qq 10
                self.user = []    # qq_hex
                self.caption = []    # qq_utf-8
                self.pas = ""
                self.md51 = []
                self.md52 = []
                self.tim = []
                self.key = []
                self.nick = ""
                self.Token002C = []
                self.Token004C = []    # A2
                self.Token0058 = []
                self.TGTKey = []
                self.shareKey = []
                self.pub_key = []
                self._ksid = []
                self.randKey = []
                self.mST1Key = []    # transport秘药
                self.stweb = ""
                self.skey = []
                self.pskey = []    # 01 6C 暂时没返回
                self.superkey = []    # 01 6D 暂时没返回
                self.vkey = []
                self.sid = []
                self.sessionKey = []
                self.loginState = 0  # 登陆是否验证成功
                self.VieryToken1 = []    # 验证码token
                self.VieryToken2 = []    # 验证码token
                self.Viery = []    # y验证码
            
        class qq_global:
            def __init__(self):
                self.imei = ""
                self.imei_ = []
                self.ver = []
                self.appId = 0
                self.pc_ver = ""
                self.os_type = ""
                self.os_version = ""
                self._network_type = 0
                self._apn = ""
                self.device = ""
                self._apk_id = ""
                self._apk_v = ""
                self._apk_sig = []
        class HeadData:
            def __init__(self):
                self.typ = 0
                self.tag = 0                # 1-10
        class JceMap:
            def __init__(self):
                self.key_type = 0
                self.key = []
                self.val_type = 0
                self.val = []
        class JceStruct_RequestPacket:
            def __init__(self):
                self.iversion = 0
                self.cPacketType = 0
                self.iMessageType = 0
                self.iRequestId = 0
                self.sServantName = ""
                self.sFuncName = ""
                self.sBuffer = []
                self.iTimeout = 0
                self.context = [JceMap()]  # 重定义下
                self.status = [JceMap()]   # 重定义下
        class JceStruct_SvcReqRegister:
            def __init__(self):
                self.lUin = 0    # 0
                self.lBid = 0    # 1
                self.cConnType = 0    # 2
                self.sOther = ""    # 3
                self.iStatus = 0    # 4
                self.bOnlinePush = 0    # 5
                self.bIsOnline = 0    # 6
                self.bIsShowOnline = 0    # 7
                self.bKikPC = 0    # 8
                self.bKikWeak = 0    # 9
                self.timeStamp = 0    # 10
                self._11 = 0    # 11
                self._12 = 0
                self._13 = ""
                self._14 = 0
                self._imei_ = []
                self._17 = 0
                self._18 = 0
                self._19_device = ""
                self._20_device = ""
                self._21_sys_ver = ""
        class JceStruct_FSOLREQ:
            def __init__(self):
                self.luin = 0
                self._1 = 0
                self._2 = 0
                self._3 = 0
                self._4 = 0
                self._5 = 0
                self._6 = 0
        class JceStruct_FriendListResp:
            def __init__(self):
                self.reqtype = 0    # 0
                self.ifReflush = 0    # 1
                self.uin = 0   # 2
                self.startIndex = 0    # 3
                self.getfriendCoun = 0    # 4
                self.totoal_friend_count = 0    # 5
                self.friend_count = 0    # 6
                self.vecFriendInfo = 0
                self.groupid = 0
                self.ifGetGroupInfo = 0
                self.groupstartIndex = 0
                self.getgroupCount = 0
                self.totoal_group_count = 0
                self.group_count = 0
                self.vecGroupInfo = 0
                self.result = 0
                self.errorCode = 0
                self.online_friend_count = 0
                self.serverTime = 0
                self.sqqOnLine_count = 0
                self.cache_vecFriendInfo = []
                self.cache_vecGroupInfo = []
        class JceStruct_GroupListResp:
            def __init__(self):
                self.a = 0
                self.b = 0
                self.c = ""
                self.d = 0
                self.e = 0
        class JceStruct_FriendInfo:
            def __init__(self):
                self.friendUin = 0
                self.groupId = 0
                self.faceId = 0
                self.name = ""
                self.online = ""
                self.sqqtype = 0
                self.status = 0
                self.memberLevel = 0
                self.isMqqOnLine = 0
                self.sqqOnLineState = 0
                self.isIphoneOnline = 0
                self.detalStatusFlag = 0
                self.sqqOnLineStateV2 = 0
                self.sShowName = ""
                self.isRemark = 0
                self.nick = ""
                self.cSpecialFlag = 0
                self.VecIMGroupID = []
                self.VecMSFGroupID = []

        class JceStruct_GroupInfo:
            def __init__(self):
                self.groupId = 0
                self.groupname = ""
                self.friend_count = 0
                self.groupqm = ""
                self.online_friend_count = 0
                self.seqid = 0
                self.sqqOnLine_count = 0
        class JceStruct_FL:
            def __init__(self):
                self._0_reqtype = 0
                self._1_ifReflush = 0
                self.luin = 0
                self._3_startIndex = 0
                self._4_getfriendCount = 0
                self._5_totoal_friend_count = 0
                self._6_friend_count = 0
                self._7 = 0
                self._8 = 0
                self._9 = 0
                self._10 = 0
                self._11 = 0
                self._12 = 0
                self._13 = 0
                self._14 = ""
        class JceStruct_ReqHeader:
            def __init__(self):
                self._0_shVersion = 0
                self._1_lMID = 0                        # qq
                self._2_appid = 0
                self._3_eBusiType = 0
                self._4_eMqqSysType = 0
                self._5 = 0
                self._6 = 0
        class RespEncounterInfo:
            def __init__(self):
                self.lEctID = 0
                self.iDistance = 0
                self.lTime = 0
                self.strDescription = ""
                self.wFace = 0
                self.cSex = 0
                self.cAge = 0
                self.strNick = ""
                self.num = 0
                self.gender = 0
                self.age = ""
                self.province = ""
                self.cGroupId = 0
                self.strPYFaceUrl = ""
                self.strSchoolName = ""
                self.strCompanyName = ""
                self.strPYName = ""
                self.nFaceNum = 0
                self.strCertification = ""
                self.shIntroType = 0
                self.vIntroContent = []
                self.vFaceID = []
                self.eMerchantType = 0
                self.iVoteIncrement = 0
                self.bIsSingle = 0
                self.iLat = 0
                self.iLon = 0
                self.iRank = 0
                self.lTotalVisitorsNum = 0
                self.cSpecialFlag = 0
        class JceStruct_ReqUserInfo:
            def __init__(self):
                self._0_vCells = [0 for i in range(4)]
                self._3_strAuthName = ""
                self._4_strAuthPassword = ""
                self._5_eListType = 0
                self._6 = 0
        class JceStruct_GpsInfo:
            def __init__(self):
                self.lat = 0
                self.lon = 0
                self.alt = 0
                self.eType = 0
                self.accuracy = [0]
        class JceStruct_GPS:
            def __init__(self):
                self._0_time = 0    # time
                self._1_luin = 0    # qq
                self._2 = 0    # 114372142
                self._3 = 0    # 4738116111738333504
                self._4 = 0    # 126427945827296800
                self._5  = ""    # 湖北省
                self._6 = 0
        class struct_msg:
            def __init__(self):
                self.typ = 0
                self.text = ""
        class struct_group_msg:
            def __init__(self):
                self.groupUin = 0
                self.sendUin = 0
                self.sendName = [0 for i in range(20)]
                self.arr = [struct_msg_type() for i in range(20)]
        class struct_msg_type:
            def __init__(self):
                self.typ = 0
                self.msg_len = 0
                self.msg = [0 for i in range(1000)]
        class CardData:
            def __init__(self):
                self.qq = 0
                self.name = ""
                self.zanMun = 0
        class JceStruct_Group_MemberList:
            def __init__(self):
                self.a = 0
                self.b = 0
                self.c = 0
        class SYSTEMTIME:        # 系统时间
            def __init__(self):
                self.year = 0
                self.month = 0
                self.week = 0
                self.day = 0
                self.hour = 0
                self.minute = 0
                self.second = 0
                self.milliseconds = 0
        class FILETIME:                # 文件时间
            def __init__(self):
                self.tim = 0
        class dk1:                # 数据类型1
            def __init__(self):
                self._0 = 0
                self._1 = 0
                self._2 = 0    # 126431811297864200
                self._3 = 0
                self._4 = 0
                self._5 = 0    # 1007531172
                self._6 = 0    # 1506
        self.qq_info = qq_info
        self.qq_global = qq_global
        self.HeadData = HeadData
        self.JceMap = JceMap
        self.JceStruct_RequestPacket = JceStruct_RequestPacket
        self.JceStruct_SvcReqRegister = JceStruct_SvcReqRegister
        self.JceStruct_FSOLREQ = JceStruct_FSOLREQ
        self.JceStruct_FriendListResp = JceStruct_FriendListResp
        self.JceStruct_GroupListResp = JceStruct_GroupListResp
        self.JceStruct_FriendInfo = JceStruct_FriendInfo
        self.JceStruct_GroupInfo = JceStruct_GroupInfo
        self.JceStruct_FL = JceStruct_FL
        self.JceStruct_ReqHeader = JceStruct_ReqHeader
        self.RespEncounterInfo = RespEncounterInfo
        self.JceStruct_ReqUserInfo = JceStruct_ReqUserInfo
        self.JceStruct_GpsInfo = JceStruct_GpsInfo
        self.JceStruct_GPS = JceStruct_GPS
        self.struct_msg = struct_msg
        self.struct_group_msg = struct_group_msg
        self.struct_msg_type = struct_msg_type
        self.CardData = CardData
        self.JceStruct_Group_MemberList = JceStruct_Group_MemberList
        self.SYSTEMTIME = SYSTEMTIME
        self.FILETIME = FILETIME
dt = dt()
if __name__  ==  "__main__":
    print dt.qq_info().QQ
    print dt.FILETIME().tim
    print "test ok!"
