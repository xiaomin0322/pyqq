# -*- coding: utf8 -*-
# 作者：Light.紫.星
# QQ：1311817771
# 翻译自 易语言 安卓QQ协议登陆
from AndroidOnly import*
from AndroidOnly import _pack
from AndroidOnly import _unpack
from dt import dt
import time,random,socket,datetime,struct,os,threading
socket.setdefaulttimeout(5000)
class JceStruct_Factory:
    def __init__(self):
        # 常量：
        self.login_state_logining = 0  # 正在登陆
        self.login_state_veriy = 1  # 需要验证码
        self.login_state_success = 2  # 验证成功
        self.TYPE_BYTE = 0
        self.TYPE_DOUBLE = 5
        self.TYPE_FLOAT = 4
        self.TYPE_INT = 2
        self.TYPE_JCE_MAX_STRING_LENGTH = 104857600
        self.TYPE_LIST = 9
        self.TYPE_LONG = 3
        self.TYPE_MAP = 8
        self.TYPE_SHORT = 1
        self.TYPE_SIMPLE_LIST = 13
        self.TYPE_STRING1 = 6
        self.TYPE_STRING4 = 7
        self.TYPE_STRUCT_BEGIN = 10
        self.TYPE_STRUCT_END = 11
        self.TYPE_ZERO_TAG = 12
        self.Event_Get_Firends = 1  # 自己的好友
        self.Event_Get_Neighbor = 2  # 附近人
    def Read_RequestPacket(self,in_,struct_):
        struct_.iversion = in_.ReadShort(1)
        struct_.cPacketType = in_.ReadShort(2)
        struct_.iMessageType = in_.ReadShort(3)
        struct_.iRequestId = in_.ReadInt(4)
        struct_.sServantName = in_.ReadString(5)
        struct_.sFuncName = in_.ReadString(6)
        struct_.sBuffer = in_.ReadSimpleList(7)
        struct_.iTimeout = in_.ReadInt(8)
        struct_.context = []
        in_.ReadMap(9, struct_.context)
        struct_.status = []
        in_.ReadMap(10, struct_.status)
    def Write_RequestPacket(self,out_,struct_):
        out_.WriteShort(struct_.iversion, 1)
        out_.WriteShort(struct_.cPacketType, 2)
        out_.WriteShort(struct_.iMessageType, 3)
        out_.WriteInt(struct_.iRequestId, 4)
        out_.WriteStringByte(struct_.sServantName, 5)
        out_.WriteStringByte(struct_.sFuncName, 6)
        out_.WriteSimpleList(struct_.sBuffer, 7)
        out_.WriteInt(struct_.iTimeout, 8)
        out_.WriteMap(struct_.context, 9)
        out_.WriteMap(struct_.status, 10)
    def Read_SvcReqRegister(self,in_,struct_):
        struct_.lUin_ = in_.ReadLong(0)
        struct_.lBid = in_.ReadLong(1)
        struct_.cConnType = in_.ReadByte(2)
        struct_.sOther = in_.ReadString(3)
        struct_.iStatus = in_.ReadInt(4)
        struct_.bOnlinePush = in_.ReadByte(5)
        struct_.bIsOnline = in_.ReadByte(6)
        struct_.bIsShowOnline = in_.ReadByte(7)
        struct_.bKikPC = in_.ReadByte(8)
        struct_.bKikWeak = in_.ReadByte(9)
        struct_.timeStamp = in_.ReadLong(10)
        
        struct_._11 = in_.ReadByte(11)
        struct_._12 = in_.ReadByte(12)
        struct_._13 = in_.ReadString(13)
        struct_._14 = in_.ReadByte(14)
        struct_._imei_ = tohex(in_.ReadSimpleList(16))
        struct_._17 = in_.ReadShort(17)
        struct_._18 = in_.ReadByte(18)
        struct_._19_device = in_.ReadString(19)
        struct_._20_device = in_.ReadString(20)
        struct_._21_sys_ver = in_.ReadString(21)
    def Write_SvcReqRegister(self,out_,struct_):
        out_.WriteLong(struct_.lUin, 0)
        out_.WriteLong(struct_.lBid, 1)
        out_.WriteByte(struct_.cConnType, 2)
        out_.WriteStringByte(struct_.sOther, 3)
        out_.WriteInt(struct_.iStatus, 4)
        out_.WriteByte(struct_.bOnlinePush, 5)
        out_.WriteByte(struct_.bIsOnline, 6)
        out_.WriteByte(struct_.bIsShowOnline, 7)
        out_.WriteByte(struct_.bKikPC, 8)
        out_.WriteByte(struct_.bKikWeak, 9)
        out_.WriteLong(struct_.timeStamp, 10)
        #print "write",out_.toByteArray ()

        out_.WriteByte(struct_._11, 11)
        out_.WriteByte(struct_._12, 12)
        out_.WriteStringByte(struct_._13, 13)
        out_.WriteByte(struct_._14, 14)
        out_.WriteSimpleList(struct_._imei_, 16)
        out_.WriteShort(struct_._17, 17)
        out_.WriteByte(struct_._18, 18)
        out_.WriteStringByte(struct_._19_device, 19)
        out_.WriteStringByte(struct_._20_device, 20)
        out_.WriteStringByte(struct_._21_sys_ver, 21)
    def Read_GetSimpleOnlineFriendInfoReq(self,in_,struct_):
        struct_.luin_ = in_.ReadLong(0)
        struct_._1 = in_.ReadShort(1)
        struct_._2 = in_.ReadShort(2)
        struct_._3 = in_.ReadShort(3)
        struct_._4 = in_.ReadShort(4)
        struct_._5 = in_.ReadShort(5)
        struct_._6 = in_.ReadShort(6)
    def Write_GetSimpleOnlineFriendInfoReq(self,out_,struct_):
        out_.WriteLong(struct_.luin_, 0)
        out_.WriteShort(struct_._1, 1)
        out_.WriteShort(struct_._2, 2)
        out_.WriteShort(struct_._3, 3)
        out_.WriteShort(struct_._4, 4)
        out_.WriteShort(struct_._5, 5)
        out_.WriteShort(struct_._6, 6)
    def Read_FL(self,in_,struct_):
        struct_._0_reqtype = in_.ReadShort(0)
        struct_._1_ifReflush = in_.ReadShort(1)
        struct_.luin_ = in_.ReadLong(2)
        struct_._3_startIndex = in_.ReadShort(3)
        struct_._4_getfriendCount = in_.ReadShort(4)
        struct_._5_totoal_friend_count = in_.ReadShort(5)
        struct_._6_friend_count = in_.ReadShort(6)
        struct_._7 = in_.ReadShort(7)
        struct_._8 = in_.ReadShort(8)
        struct_._9 = in_.ReadShort(9)
        struct_._10 = in_.ReadShort(10)
        struct_._11 = in_.ReadShort(11)
    def Write_FL(self,out_,struct_):
        out_.WriteShort(struct_._0_reqtype, 0)
        out_.WriteShort(struct_._1_ifReflush, 1)
        out_.WriteLong(struct_.luin_, 2)
        out_.WriteShort(struct_._3_startIndex, 3)
        out_.WriteShort(struct_._4_getfriendCount, 4)
        out_.WriteShort(struct_._5_totoal_friend_count, 5)
        out_.WriteShort(struct_._6_friend_count, 6)
        out_.WriteShort(struct_._7, 7)
    def Read_FLRESP(self,b,struct_,friends):
        i = 0;t_arr = "";t_type = 0;t_count = 0;in_ = JceInputStream();
        flinfo = dt.JceStruct_FriendInfo();o = [];
        in_.wrap(b)
        in_.ReadByte(0)  # OA
        struct_.reqtype = in_.ReadByte(0)
        struct_.ifReflush = in_.ReadByte(1)
        struct_.uin_ = in_.ReadLong(2)
        struct_.startIndex = in_.ReadShort(3)
        struct_.getfriendCount = in_.ReadShort(4)
        struct_.totoal_friend_count = in_.ReadShort(5)
        struct_.friend_count = in_.ReadShort(6)
        t_type = in_.ReadToTag(7)
        if(t_type != self.TYPE_ZERO_TAG):
            if(t_type == self.TYPE_LIST):
                t_count = in_.ReadShort(0)
                for i in range(t_count):
                    in_.ReadByte(0)    # OA
                    flinfo.friendUin_ = in_.ReadLong(0)
                    # print(“friendUin_”, flinfo.friendUin_)
                    flinfo.groupId = in_.ReadByte(1)
                    # print(“groupId”, flinfo.groupId)
                    flinfo.faceId = in_.ReadShort(2)
                    # print(“faceId”, flinfo.faceId)
                    flinfo.name = in_.ReadString(3)
                    # print(“name”, flinfo.name)
                    flinfo.sqqtype = in_.ReadByte(4)
                    # print(“sqqtype”, flinfo.sqqtype)
                    flinfo.status = in_.ReadByte(5)
                    # print(“status”, flinfo.status)
                    flinfo.memberLevel = in_.ReadByte(6)
                    # print(“memberLevel”, flinfo.memberLevel)
                    flinfo.isMqqOnline = in_.ReadByte(7)
                    # print(“isMqqOnline”, flinfo.isMqqOnline)
                    flinfo.sqqOnlineState = in_.ReadByte(8)
                    # print(“sqqOnlineState”, flinfo.sqqOnlineState)
                    flinfo.isIphoneOnline = in_.ReadByte(9)
                    # print(“isIphoneOnline”, flinfo.isIphoneOnline)
                    flinfo.detalStatusFlag = in_.ReadByte(10)
                    # print(“detalStatusFlag”, flinfo.detalStatusFlag)
                    flinfo.sqqOnlineStateV2 = in_.ReadByte(11)
                    # print(“sqqOnlineStateV2”, flinfo.sqqOnlineStateV2)
                    flinfo.sShowName = in_.ReadString(12)
                    # print(flinfo.friendUin_, flinfo.groupId, flin_fo.name, flin_fo.status)
                    in_.ReadShort(13)                  # 暂停()
                    flinfo.nick = in_.ReadString(14) # 好友昵称
                    # print(flinfo.nick)
                    friends.append(flinfo)
                    in_.skipToEnd()
    def Write_ReqGetEncounte(self,t_out,isFirst,gender,star,age_low,age_high,last_time_minute,last_flush_time):# 获取附近人
        # ,,2性别0全部 1女 2难,14星座0全部 1水平 双鱼 。。。,15年龄低,16年龄高,17最近在线480为全部,,
        t_bin = [];t_bin_1 = [];
        t_out.WriteByte(0, 0)
        t_out.WriteInt(900000000, 1)
        t_out.WriteInt(900000000, 2)
        t_out.WriteByte(0, 3)
        t_out.WriteByte(0, 4)
        t_out.WriteStringByte("", 5)
        t_bin_1 = t_out.toByteArray()
        
        t_out.WriteByte(0, 0)
        t_out.WriteByte(0, 1)
        t_out.WriteByte(255, 2)
        t_out.WriteByte(0, 3)
        t_bin = t_out.toByteArray()
        t_out.clear()
        
        t_out.WriteJceStruct(t_bin, 0)
        t_out.WriteStringByte("B1_QQ_Neighbor_android", 3)
        t_out.WriteStringByte("NzVK_qGE", 4)
        t_out.WriteByte(0, 5)
        t_out.WriteByte(2, 6)
        t_out.putHex("89 00 0A 0A 03 00 00 12 68 9D 42 32 5D 10 F3 0B 0A 03 00 00 0C 82 68 CD 63 BC 10 CE 0B 0A 03 00 00 EC 17 2F 1E CC 04 10 CB 0B 0A 03 00 00 28 2C B2 4C 49 5C 10 BA 0B 0A 03 00 00 C8 3A 35 53 4D 20 10 B8 0B 0A 03 00 00 C8 3A 35 56 44 A8 10 B1 0B 0A 03 00 00 0C 82 68 9E D6 12 10 B1 0B 0A 03 00 00 CC 34 29 25 61 1E 10 AA 0B 0A 03 00 00 D0 C7 C0 6B 27 58 10 AA 0B 0A 03 00 00 9C 21 6A 55 F6 80 10 AA 0B 99 0C")  # 这里包含附近人wifi
        
        t_bin = t_out.toByteArray()
        t_out.clear()
        
        t_out.WriteJceStruct(t_bin, 0)
        t_out.WriteJceStruct(t_bin_1, 1)
        t_out.WriteByte(0, 2)
        t_out.WriteByte(255, 3)
        t_out.WriteSimpleList({ 0 }, 5)
        t_out.WriteShort(0, 6)
        t_out.WriteShort(2000, 7)
        t_out.WriteByte(255, 8)
        t_out.WriteByte(0, 9)
        # t_out.putHex("BD 00 01 01 0A 00 00 01 0A 10 03 2C 3C 40 01 56 1C 50 75 62 41 63 63 6F 75 6E 74 53 76 63 2E 6E 65 61 72 62 79 5F 70 75 62 61 63 63 74 66 0E 6E 65 61 72 62 79 5F 70 75 62 61 63 63 74 7D 00 01 00 C8 08 00 01 06 0E 6E 65 61 72 62 79 5F 70 75 62 61 63 63 74 1D 00 01 00 B0 0A 00 02 1D 00 0C 20 02 3A 0A 0C 1C 20 FF 3C 0B 19 00 0A 0A 03 00 00 12 68 9D 42 32 5D 10 F3 0B 0A 03 00 00 0C 82 68 CD 63 BC 10 CE 0B 0A 03 00 00 EC 17 2F 1E CC 04 10 CB 0B 0A 03 00 00 28 2C B2 4C 49 5C 10 BA 0B 0A 03 00 00 C8 3A 35 53 4D 20 10 B8 0B 0A 03 00 00 C8 3A 35 56 44 A8 10 B1 0B 0A 03 00 00 0C 82 68 9E D6 12 10 B1 0B 0A 03 00 00 CC 34 29 25 61 1E 10 AA 0B 0A 03 00 00 D0 C7 C0 6B 27 58 10 AA 0B 0A 03 00 00 9C 21 6A 55 F6 80 10 AA 0B 29 0C 3A 06 0F 38 36 38 33 33 31 30 31 34 39 36 36 39 36 34 16 00 26 00 0B 0B 0B 8C 98 0C A8 0C")
        
        t_out.WriteByte(0, 12)
        t_out.WriteShort(0, 13)
        t_out.WriteByte(0, 14)  # 14星座0全部 1水平 双鱼 。。。。
        t_out.WriteShort(0, 15)  #  15年龄低
        t_out.WriteShort(0, 16)  #  16年龄高
        t_out.WriteShort(480, 17)  # 17最近在线480为全部
        return t_out
    def Read_FSRESP(self,b,t_verify_type,question,friendUin):
        in_ = JceInputStream();t_type = 0;t_count = 0;
        """
        ' [0 2 ]414491068
        ' [1 2 ]1197413597  需要加的好友
        ' [2 0 ]1   验证类型 0允许任何人  1需要验证信息  3 需要正确回答问题  4需要回答问题并由我确定
        ' [3 9 ][      ]  数组的第一个是问题。
        ' [4 12 ]0
        ' [5 12 ]0
        ' [6 13 ]
        ' [7 12 ]0
        ' [8 13 ]
        """
        in_.wrap(b)
        in_.ReadByte(0)
        in_.ReadLong(0)
        friendUin_ = in_.ReadLong(1)
        t_verify_type = in_.ReadByte(2)
        t_type  = in_.ReadType()
        if(t_type == self.TYPE_ZERO_TAG):
            pass
        elif(t_type == self.TYPE_LIST):
            t_count  = in_.ReadShort(0)
            if(t_count>0):
                question  = in_.ReadString(0)
        return t_verify_type,question,friendUin
    def Read_AFRESP(self,b,suc,msg):
        in_ = JceInputStream();t_type = 0;t_count = 0;
        """
        ' [0 10 ]
        ' [0 2 ]414491068
        ' [1 12 ]0 uin
        ' [2 12 ]0  typ
        ' [3 0 ]1
        ' [4 0 ]1
        ' [6 0 ]1  0成功
        ' [7 1 ]255  0成功
        ' [8 6 ]添加失败，请稍后再试
        ' [9 13 ]
        ' [10 13 ]
        ' [11 13 ]
        """
        in_.wrap(b)
        in_.ReadByte(0)
        in_.ReadLong(0)
        in_.ReadByte(1)
        in_.ReadByte(2)
        in_.ReadShort(3)
        in_.ReadShort(4)
        in_.ReadShort(6)
        t_type = in_.ReadShort(7)
        msg = in_.ReadString(8)
        if(t_type == 0):
            suc = 1
        return suc,msg
    def Read_GroupMngRes(self,b): # 获取群列表，懒得分析，随便写的，有点粗糙
        in_ = JceInputStream();t_type = 0;t_count = 0;
        t_group = dt.JceStruct_GroupInfo();i = 0
        bzw = "";bao = "";zbao = "";qunhao = [];quname = [];
        qunmc = "";flag = 0;
        bzw = tohex(b)
        bao = bzw[:bzw.find("6900")+4]
        zbao = zbao.replace(binmid(bao,"0A020C","1200"),"")
        zbao = zbao.replace(binmid(zbao,"2C31","46"),"")
        """  文本_取中间_批量_正则方式(主包体, “12”, “2C”, 群号码数组)
                ' 调试输出(主包体)
                文本_取中间_批量_正则方式(主包体, “46”, “56”, 群名称数组)
                .计次循环首(取数组成员数(群号码数组), i)
                    群名称 = iconv.Utf8ToAnsi(字节集替换(十六进制文本到字节集(删全部空(群名称数组 [i])), 1, 1, {  }))
                    表项索引 = _启动窗口.超级列表框_群列表.插入表项(, , , , , )
                    _启动窗口.超级列表框_群列表.置标题(表项索引, 0, 到文本(表项索引 ＋ 1))
                    _启动窗口.超级列表框_群列表.置标题(表项索引, 1, 到文本(进制_十六到十(删全部空(群号码数组 [i]))))
                    _启动窗口.超级列表框_群列表.置标题(表项索引, 2, 子文本替换(群名称, “?”, “”, , , 真))
                .计次循环尾()
          """
    def Read_EncounterSvc_RespGetEncounterV2(self,b,Neighbor):  # EncounterSvc_RespGetEncounterV2
        in_ = JceInputStream();t_type = 0;t_count = 0;t_bin = [];
        i = 0;t_Neighbor = dt.RespEncounterInfo();QQ = 0;
        print "努力获取附近人中，请稍候!"
        in_.wrap(b)
        # 置剪辑板文本(字节集到十六进制文本(bin))
        in_.ReadByte(0)  #  OA
        #  --0-
        in_.ReadInt(0)  #  0 获取时间
        #  -----1
        t_type = in_.ReadType()
        if(t_type == self.TYPE_STRUCT_BEGIN):
            in_.ReadLong(0)  #  1412558304
            in_.ReadLong(1)  #  30530821
            in_.ReadLong(2)  #  114372161
            in_.ReadLong(3)  #  4738116111738333504
            in_.ReadLong(4)
            t_Neighbor.provin_ce = in_.ReadString(5)  #  省份
            print(t_Neighbor.provin_ce)
            t_b = in_.ReadSimpleList(6)
        in_.ReadType()  #  OB
        t_type = in_.ReadType()
        if(t_type == self.TYPE_LIST):
            t_count = in_.ReadShort(0)
            for i in range(t_count):
                in_.ReadByte(0)
                t_Neighbor.num = in_.ReadLong(0)
                in_.ReadShort(1)
                in_.ReadInt(2)
                t_Neighbor.strDescription = in_.ReadString(3)
                in_.ReadShort(4)
                t_Neighbor.gender = in_.ReadShort(5)
                
                t_Neighbor.age = str(in_.ReadShort(6))
                print(t_Neighbor.age)
                t_Neighbor.strNick = in_.ReadString(7)
                in_.ReadByte(8)
                Neighbor.append(t_Neighbor)
                in_.skipToEnd()
        return Neighbor
    def Read_applist(self,b):
        ssnr = []
        """
                .局部变量 说说内容数组, 文本型, , "0"
                .局部变量 说说内容, 文本型
                .局部变量 说说标识数组, 文本型, , "0"
                .局部变量 说说标识, 文本型
                .局部变量 i, 整数型
                .局部变量 表项索引, 整数型
                .局部变量 包体, 文本型
                .局部变量 解开包体, 文本型
                
                ' 调试输出(字节集到十六进制文本(bin))
                文本_取中间_批量_正则方式(字节集到十六进制文本(bin), “16 00 00 04 1D 00 00”, “1C 2C 39 0C”, 说说内容数组)
                文本_取中间_批量_正则方式(字节集到十六进制文本(bin), “06 18”, “16 00”, 说说标识数组)
                ' 调试输出(说说内容数组)
                _启动窗口.超级列表框_说说列表.全部删除()
                .计次循环首(取数组成员数(说说内容数组), i)
                    说说内容 = 取文本右边(说说内容数组 [i], 取文本长度(说说内容数组 [i]) － 9)
                    说说内容 = 编码_Utf8到Ansi(十六进制文本到字节集(删全部空(说说内容)))
                    说说标识 = 编码_Utf8到Ansi(十六进制文本到字节集(删全部空(说说标识数组 [i])))
                    ' 调试输出(说说标识)
                    表项索引 = _启动窗口.超级列表框_说说列表.插入表项(, , , , , )
                    _启动窗口.超级列表框_说说列表.置标题(表项索引, 0, 到文本(表项索引 ＋ 1))
                    _启动窗口.超级列表框_说说列表.置标题(表项索引, 1, 子文本替换(说说内容, “?”, “”, , , 真))
                    _启动窗口.超级列表框_说说列表.置标题(表项索引, 2, 子文本替换(说说标识, “?”, “”, , , 真))
                .计次循环尾()

        """
    def Read_GroupMngRes2(self,b):
        pass
    """
                    .局部变量 in, JceInputStream
                    .局部变量 t_type, 整数型
                    .局部变量 struct, JceStruct_GroupListResp
                    .局部变量 t_bin, 字节集
                    .局部变量 q_name, 文本型
                    .局部变量 q_uin, 长整数型
                    .局部变量 q_code, 长整数型
                    .局部变量 i, 整数型
                    .局部变量 j, 整数型
                    .局部变量 数组, 文本型, , "0"
                    .局部变量 群号码, 文本型, , "0"
                    .局部变量 群名称, 文本型, , "0"
                    .局部变量 群Code, 文本型, , "0"
                    .局部变量 群数量, 整数型
                    .局部变量 首bin, 字节集
                    .局部变量 去掉长度, 整数型
                    .局部变量 表项, 整数型
                    .局部变量 k, 整数型
                    
                    群二次获取 = 十六进制文本到字节集(“00” ＋ 删全部空(取文本右边(文本_取出中间文本(字节集到十六进制文本(bin), “2C 3C 4D”, “59 00”, 1, ), 取文本长度(删全部空(文本_取出中间文本(字节集到十六进制文本(bin), “2C 3C 4D”, “59 00”, 1, ))) － 6)))
                    调试输出(字节集到十六进制文本(群二次获取))
                    首bin = 十六进制文本到字节集(删全部空(文本_取左边(字节集到十六进制文本(bin), “0B 69”, 1, )) ＋ “0B”)
                    置剪辑板文本(字节集到十六进制文本(bin))
                    群数量 = 进制_十六到十(取文本右边(文本_取出中间文本(删全部空(字节集到十六进制文本(bin)), 进制_十到十六(到数值(_启动窗口.编辑框_账号.内容)), “2C3C4D”, 1, ), 2))
                    bin = 字节集替换(首bin, 1, 取文本长度(删全部空(文本_取左边(字节集到十六进制文本(首bin), “59 00”, 1, ))) ÷ 2, {  })
                    bin = 字节集替换(bin, 1, 3, {  })
                    
                    in.wrap(bin)
                    .计次循环首(群数量, i)
                        in.ReadByte(0)
                        q_code = in.ReadLong(0)
                        q_uin = in.ReadLong(1)
                        in.ReadInt(2)
                        in.ReadInt(3)
                        q_name = in.ReadString(4)
                    
                        .如果真(取文本长度(到文本(q_uin)) ＞ 1)
                            加入成员(群号码, 到文本(q_uin))
                            加入成员(群Code, 到文本(q_code))
                            加入成员(群名称, q_name)
                        .如果真结束
                    
                        in.ReadString(5)
                        in.ReadLong(6)
                        in.ReadInt(7)
                        in.ReadInt(8)
                        in.ReadInt(9)
                        in.ReadInt(10)
                        in.ReadInt(11)
                        in.ReadInt(12)
                        in.ReadInt(13)
                        in.ReadInt(14)
                        in.ReadInt(15)
                        in.ReadInt(16)
                        in.ReadInt(17)
                        in.skipToEnd()
                    .计次循环尾()
                    
                    .' 如果(取字节集长度(群二次获取) ≥ 2)
                        ' 二次取群()
                    
                    .否则
                        .如果(取数组成员数(群号码) ≠ 0)
                            .计次循环首(取数组成员数(群号码), k)
                                _启动窗口.超级列表框_群列表.插入表项(, , , , , )
                                _启动窗口.超级列表框_群列表.置标题(k － 1, 0, 到文本(k))
                                _启动窗口.超级列表框_群列表.置标题(k － 1, 1, 群号码 [k])
                                _启动窗口.超级列表框_群列表.置标题(k － 1, 2, 群名称 [k])
                                _启动窗口.超级列表框_群列表.置标题(k － 1, 3, 群Code [k])
                            .计次循环尾()
                        .否则
                    
                        .如果结束
    """
    def Read_GroupMemberList(self,b):
        MemberList = dt.JceStruct_Group_MemberList();t_type = 0;
        in_ = JceInputStream();i = 0;flag = 0;name = "";age = 0;
        uin = 0;name2 = "";sex = 0;
        in_.wrap(b)
        in_.ReadByte(0)  #  OA
        MemberList.a = in_.ReadLong(0)
        MemberList.b = in_.ReadLong(1)
        MemberList.c = in_.ReadLong(2)
        t_type = in_.ReadToTag(3)
        flag = in_.ReadByte(0)
        print flag
        for i in range(flag):
            print i
            in_.ReadByte(0)
            uin = in_.ReadLong(0)
            print uin
            in_.ReadInt(1)
            age = in_.ReadShort(2)
            print age
            sex = in_.ReadShort(3)
            if(sex == 0):print "男"
            if(sex == 1):print "女"
            name = in_.ReadString(4)
            print name
            in_.ReadShort(5)
            in_.ReadString(6)
            in_.ReadString(8)
            in_.ReadShort(9)
            in_.ReadString(10)
            in_.ReadString(11)
            in_.ReadString(12)
            name2 = in_.ReadString(13)
            in_.ReadShort(14)
            in_.ReadLong(15)
            in_.ReadLong(16)
            in_.ReadShort(17)
            in_.ReadShort(18)
            in_.ReadShort(19)
            in_.ReadShort(20)
            in_.ReadShort(21)
            in_.ReadShort(22)
            in_.ReadString(23)
            in_.ReadShort(24)
            in_.ReadString(25)
            in_.ReadShort(4)
            in_.ReadShort(5)
            in_.ReadShort(6)
            in_.ReadShort(7)
            in_.skipToEnd()
    def Read_onlinefriendList(self,b):
        in_ = JceInputStream();flag = 0;t_type = 0;i = 0;
        uin = 0;zxzt = "";c = 0;
        in_.wrap(b)
        print b
        in_.ReadByte(0)
        in_.ReadLong(0)
        t_type = in_.ReadToTag(1)
        flag = in_.ReadByte(0)
        print flag
        for i in range(flag):
            in_.ReadByte(0)
            uin_ = in_.ReadLong(0)
            # 状态表项 = _启动窗口.超级列表框_好友列表.查找表项(到文本(uin_), 1, 真, 1)
            print uin
            in_.ReadInt(1)
            in_.ReadInt(2)
            in_.ReadInt(3)
            in_.ReadInt(4)
            in_.ReadInt(5)
            in_.ReadInt(6)
            in_.ReadString(7)
            in_.ReadInt(8)
            in_.ReadInt(9)
            in_.ReadInt(10)
            in_.ReadInt(11)
            in_.ReadInt(12)
            in_.ReadInt(13)
            zxzt = in_.ReadString(14)
            print zxzt
            in_.skipToEnd()
    def Read_DiscussRespHeader(self,b):
        in_ = JceInputStream()
        in_.wrap(b)
        b = b[len(b)-31:]
        b = b[:4]
        print "恭喜！讨论组创建成功,讨论组ID为：",tohex(b)
    def Read_ReqAddDiscussMember(self,b):
        in_ = JceInputStream();
        in_.wrap(b)
    def Read_RespGetDiscuss(self,b):
        in_ = JceInputStream();bt = "";flag = 0;
        id = 0;i = 0;t_type = 0;
        bt = tohex(b)
        bt = binmid(bt,"5151536572766963652E5265737047657444697363757373","8C980CA80C")
        bt = bt[8:]
        flag = int(hex(bt[:8][6:]),16)
        b = tozjj(bt)
        print tohex(b)
        in_.wrap(b)
        in_.ReadByte(0)
        t_type = in_.ReadToTag(0)
        in_.ReadByte(0)
        for i in range(flag):
            in_.ReadByte(0)
            id = in_.ReadLong(0)
            print "讨论组id", id
            in_.ReadShort(1)
            in_.ReadToTag(1)
            in_.skipToEnd()
    def Read_MainPage_rq(self,b):
        in_ = JceInputStream();main_long = 0;t_arr = [];t_qq = 0;
        t_jce = dt.JceMap();t_type = 0;main = "";Popularity = 0;qdcd = 0;
        qdcd =  len(b[:b.find("789C")+4])-2
        """
                bin = 字节集替换(bin, 1, 去掉长度, {  })
                main_long = 进制_十六到十(删全部空(字节集到十六进制文本(取字节集左边(bin, 2))))
                bin = 字节集替换(bin, 1, 2, {  })
                bin = 取字节集左边(bin, main_long)
                调试输出(“到解压了”)
                bin = inflate_Decompress(bin)
                调试输出(字节集到十六进制文本(bin))
                bin = 字节集替换(bin, 1, 64, {  })
                main_long = 进制_十六到十(删全部空(字节集到十六进制文本(取字节集左边(bin, 2))))
                bin = 字节集替换(bin, 1, 2, {  })
                bin = 取字节集左边(bin, main_long)
                ' -------------------------------------------------------------------------------------------------------------------------
                main = 删全部空(文本_取出中间文本(字节集到十六进制文本(bin), “FF 0B 3A 0C”, “5C 0B 4A 0C”))
                main = “3A 0C” ＋ main ＋ “5C 0B”
                bin = 十六进制文本到字节集(删全部空(main))
                调试输出(字节集到十六进制文本(bin))
                in.wrap(bin)
                in.ReadToTag(3)
                in.ReadByte(0)
                in.ReadByte(1)
                Popularity = in.ReadLong(2)
                调试输出(“当前人气数量”, Popularity)
       """
class Android(JceStruct_Factory):
    def __init__(self):
        JceStruct_Factory.__init__(self)
        self.address = ("113.108.90.53",8080)    # 服务器IP，端口
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp()        # TCP
        self.qq = dt.qq_info()
        self.gb = dt.qq_global()
        self.tlv = Tlv_()
        self.RequestId = 10000
        self.pc_sub_cmd = 0
        self.last_error = ""
        self.m_friends = [dt.JceStruct_FriendInfo()]
        self.m_Neighbor = [dt.RespEncounterInfo()]
        self.m_bin = []
        
        # 常量：
        self.login_state_logining = 0  # 正在登陆
        self.login_state_veriy = 1  # 需要验证码
        self.login_state_success = 2  # 验证成功
        self.TYPE_BYTE = 0 
        self.TYPE_DOUBLE = 5 
        self.TYPE_FLOAT = 4 
        self.TYPE_INT = 2 
        self.TYPE_JCE_MAX_STRING_LENGTH = 104857600 
        self.TYPE_LIST = 9 
        self.TYPE_LONG = 3 
        self.TYPE_MAP = 8 
        self.TYPE_SHORT = 1 
        self.TYPE_SIMPLE_LIST = 13 
        self.TYPE_STRING1 = 6 
        self.TYPE_STRING4 = 7 
        self.TYPE_STRUCT_BEGIN = 10 
        self.TYPE_STRUCT_END = 11 
        self.TYPE_ZERO_TAG = 12 
        self.Event_Get_Firends = 1  # 自己的好友
        self.Event_Get_Neighbor = 2  # 附近人
        self.kjdz = "68 74 74 70 3A 2F 2F 75 73 65 72 2E 71 7A 6F 6E 65 2E 71 71 2E 63 6F 6D 2F"   # 空间地址
        self.mood = "2F 6D 6F 6F 64 2F"
        self.gdz = "3C 41 01 37 58 00 08 00 30 16 01 30 00 04 16 00 00 05 16 41"   # 固定值
        self.findpeople = "0A 0C 1C"
    def init(self,qquser,qqpass):
        self.qq.Account = qquser
        luin = int(qquser)
        if(luin>2147483647):
            self.qq.user = Xbin.flip(tozjj(luin,"int"))[:4]# 取字节集右边(Xbin.Flip(到字节集(luin)), 4)
        else:
            iuin = luin
            self.qq.user = Xbin.flip(tozjj(iuin,"int"))# Xbin.Flip(到字节集(iuin))
        self.qq.QQ = long(qquser)
        # print "qq.user",tohex(self.qq.user),self.qq.user
        
        self.qq.caption = tozjj(str(qquser),"str")
        # print tozjj(str(qquser),"str"),tozjj(str(qquser),"str2")
        # print self.qq.caption
        self.qq.pas = qqpass
        self.qq.md51 = Hash.md5_bin(qqpass)
        # print "md51",self.qq.md51,tohex(self.qq.md51)
        self.qq.md52 = Hash.md5_bin(list2str(self.qq.md51)+list2str([0,0,0,0])+list2str(self.qq.user))
        self.qq._ksid = tozjj("93 AC 68 93 96 D5 7E 5F 94 96 B8 15 36 AA FE 91")
        # print "ksid1",self.qq._ksid
        self.gb.imei = "866819027236658"
        self.gb.ver = tozjj("5.8.0.157158","str")
        # print self.gb.ver
        self.gb.appId = 537042771
        self.gb.pc_ver = "1F41"
        self.gb.os_type = "android"
        self.gb.os_version = "4.4.4"
        self.gb._network_type = 2
        self.gb._apn = "wifi"
        self.gb.device = "vivo X5Max+"
        self.gb._apk_id = "com.tencent.mobileqq"
        self.gb._apk_v = "5.8.0.157158"
        self.gb._apk_sig = tozjj("A6 B7 45 BF 24 A2 C2 77 52 77 16 F6 F3 6E B6 8D")
        self.gb.imei_ = tozjj("38 36 36 38 31 39 30 32 37 32 33 36 36 35 38")
        # print "imei",self.gb.imei_,self.gb._apk_sig
        self.RequestId = 10000
        self.qq.Token002C = []
        self.qq.Token004C = []
        self.qq.key = [0 for i in range(16)]
    def Read_people(self,b):  #解开关键字找到的人
        return b
    def tcp(self,method = "",data = "",tim = 0):
        if(method == "connect"):
            if(self.sock.connect_ex(self.address) == 0):
                return 1
            else:
                return 0
        elif(method == "disconnect"):
            self.sock.close()
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif(method == "send"):
            self.sock.sendall(list2str(data))
        elif(method == "rec"):
            dat = self.sock.recv(20480)
            return tozjj(dat.encode("hex"))
        else:
            pass
    def getLastError(self):
        return self.last_error
    def getSubCmd(self):
        if(self.pc_sub_cmd> 2147483647):
            self.pc_sub_cmd = 0
        self.pc_sub_cmd = self.pc_sub_cmd + 1
        return(self.pc_sub_cmd)
    def Make_login_sendSsoMsg(self,servicecmd,wupbuffer,ext_bin,imei,ksid,ver,islogin):       # 登陆使用
        pk = _pack();msgcookies = tozjj("B6CC78FC");tmp = []
        #print "ml",servicecmd,wupbuffer,ext_bin,imei,ksid,ver,islogin
        pk.Empty()
        #print "self.RequestId",self.RequestId
        pk.SetInt(self.RequestId)
        pk.SetInt(self.gb.appId)
        pk.SetInt(self.gb.appId)
        pk.SetHex("01 00 00 00 00 00 00 00 00 00 00 00")
        
        pk.SetInt(len(ext_bin) + 4)
        pk.SetBin(ext_bin)
        
        pk.SetInt(len(servicecmd) + 4)
        pk.SetBin(tozjj(servicecmd,"str"))
        
        pk.SetInt(len(msgcookies) + 4)
        pk.SetBin(msgcookies)
        
        pk.SetInt(len(imei) + 4)
        pk.SetBin(tozjj(imei,"str"))
        # print "imei",tozjj(imei,"str")
        pk.SetInt(len(ksid) + 4)
        pk.SetBin(ksid)
        
        pk.SetShort(len(ver) + 2)
        pk.SetBin(ver)
        
        tmp = pk.GetAll()
        pk.Empty()
        pk.SetInt(len(tmp) + 4)
        pk.SetBin(tmp)
        tmp = pk.GetAll()
        # print "tmp",tmp
        
        pk.Empty()
        pk.SetBin(tmp)
        pk.SetInt(len(wupbuffer) + 4)
        pk.SetBin(wupbuffer)
        if(islogin == 1):islogin = 0
        else:islogin = 1
        #print "wupbuffer",wupbuffer
        #print "qian",pk.GetAll(), self.qq.key
        #print "islogin",islogin
        t=Hash.QQTEA(pk.GetAll(), self.qq.key)
        #print "lllMake_login_sendSsoMsg-t1" , t
        t=self.Pack((t), islogin)
        #print "lllMake_login_sendSsoMsg-t2" , t
        return (t)
    def Make_sendSsoMsg(self,serviceCmd,wupBuffer):
        pk = _pack();msgCookies = tozjj("B6CC78FC");tmp = [];
        pk.Empty()
        pk.SetInt(len(serviceCmd) + 4)
        #print "a0" , len( pk.GetAll( ) ) , pk.GetAll( )
        pk.SetBin(tozjj(serviceCmd,"str",0))
        #print "a1" , len( pk.GetAll( ) ) , pk.GetAll( )
        pk.SetInt(len(msgCookies) + 4)
        pk.SetBin(msgCookies)
        #print "a2" , len( pk.GetAll( ) ) , pk.GetAll( )
        tmp = pk.GetAll()
        pk.Empty()
        pk.SetInt(len(tmp) + 4)
        pk.SetBin(tmp)
        #print "a3" , len( pk.GetAll( ) ) , pk.GetAll( )
        pk.SetBin(wupBuffer)
        #print len(wupBuffer),wupBuffer
        #print "a",len(pk.GetAll()),pk.GetAll()
        t=Hash.QQTEA(pk.GetAll(), self.qq.key)
        #print "Make_sendSsoMsg - t " ,len(t) ,t,len(self.qq.key),self.qq.key
        t=self.Pack(t, 2)
        return(t)

    def Make_sendSsoMsg_simple(self,serviceCmd,iversion, iRequestId, sServantName, sFuncName, mapKey, wupBuffer):      # 一个key
        return self.Make_sendSsoMsg(serviceCmd, self.Pack_sendSsoMsg_simple(iversion, iRequestId, sServantName, sFuncName, mapKey, wupBuffer))
    def Pack(self,b,typ):
        pk = _pack()
        pk.Empty()
        #print "self.qq.Token002C",self.qq.Token002C
        if(typ == 0):
            pk.SetHex("00 00 00 08 02 00 00 00 04")
        elif(typ == 1):
            pk.SetHex("00 00 00 08 01 00 00")
            pk.SetShort(len(self.qq.Token002C) + 4)
            pk.SetBin(self.qq.Token002C)
        else:
            pk.SetHex("00 00 00 09 01")
            pk.SetInt(self.RequestId)
        pk.SetHex("00 00 00")
        pk.SetShort(len(self.qq.caption) + 4)
        pk.SetBin(self.qq.caption)
        pk.SetBin(b)
        b = pk.GetAll()
        pk.Empty()
        pk.SetInt(len(b) + 4)
        pk.SetBin(b)
        b = pk.GetAll()
        # print "b",b
        return b
    def Pack_friendlist_getFriendGroupList(self,getfriendCount,startIndex):
        struct_ = dt.JceStruct_FL();out_=JceOutputStream();b=[];
        struct_._0_reqtype = 3
        struct_._1_ifReflush = 1
        struct_.luin = self.qq.QQ
        struct_._3_startIndex = startIndex
        struct_._4_getfriendCount = getfriendCount
        struct_._6_friend_count = 1
        struct_._10 = 1
        struct_._11 = 5
        self.Write_FL( out_ ,struct_)
        b = out_.toByteArray( )
        return (self.Make_sendSsoMsg_simple( "friendlist.getFriendGroupList" , 3 , 2014428573 ,
            "ms.qq.IMService.FriendListServiceServantObj" , "GetFriendListReq" , "FL" , b ))
    def Pack_MessageSvc_SendGroupMsg(self,num,msg):
        out_ = JceOutputStream( );b = [ ];u = [ ];
        u = tozjj( msg , "str" , 0 )
        out_.WriteLong( self.qq.QQ , 0 )
        out_.WriteLong( long(num) , 1 )
        out_.WriteStringByte( msg, 2 )
        out_.WriteInt( 1 , 3 )
        out_.WriteSimpleList( u , 4 )
        out_.WriteInt( 0 , 5 )
        out_.WriteInt( 0 , 6 )
        out_.WriteInt( 0 , 7 )
        out_.WriteInt( 0 , 8 )
        out_.WriteInt( 0 , 9 )
        out_.WriteInt( 0 , 10 )
        out_.WriteInt( 0 , 11 )
        out_.WriteInt( 0 , 12 )
        out_.WriteInt( 0 , 13 )
        b = out_.toByteArray()
        t = self.Make_sendSsoMsg_simple( "MessageSvc.SendGroupMsg" , 3 , self.RequestId , "MessageSvc" , "SendGroupMsg" ,
            "req_SendGroupMsg" , b )
        return (t)
    def Pack_MessageSvc_offlinemsg(self,qqnum,msg):
        out_ = JceOutputStream();b = [];u = [];
        #msg="你好"
        u=tozjj(msg,"str",0)
        #print "utf",u
        out_.WriteLong(self.qq.QQ, 0)
        out_.WriteLong(self.qq.QQ, 1)
        out_.WriteLong(qqnum, 2)
        #out_.WriteLong(long(time.time()),3)
        out_.WriteLong(1459258561, 3 )
        #print "bbba1" , len( out_.toByteArray() ) , out_.toByteArray()
        out_.WriteStringByte(msg,4)
        #print "bbba2" , len( out_.toByteArray() ) , out_.toByteArray()
        out_.WriteStringByte("", 5)
        out_.WriteInt(0, 6)
        out_.WriteInt(0, 7)
        out_.WriteInt(1, 8)
        #print "bbba3" , len( out_.toByteArray( ) ) , out_.toByteArray( )
        out_.WriteSimpleList(u, 9)
        #print "bbba4" , len( out_.toByteArray( ) ) , out_.toByteArray( )
        out_.WriteInt(0, 10)
        out_.WriteInt(0, 11)
        out_.WriteInt(0, 12)
        out_.WriteInt(0, 14)
        b = out_.toByteArray()
        #print "bbba",len(b),b
        t=self.Make_sendSsoMsg_simple("MessageSvc.offlinemsg", 3, self.RequestId, "MessageSvc", "offlinemsg", "req_offlinemsg", b)
        #print "Pack_MessageSvc_offlinemsg",t
        return(t)
    def Pack_sendSsoMsg_simple(self,iversion, iRequestId, sServantName, sFuncName, mapKey, wupBuffer):# 一个key
        #print "pksendssm",iversion , iRequestId , sServantName , sFuncName , mapKey , wupBuffer
        req = dt.JceStruct_RequestPacket();
        out_ = JceOutputStream();
        m = [dt.JceMap()];b = [];pk = _pack()

        out_.clear()
        out_.WriteJceStruct(wupBuffer, 0)
        b = out_.toByteArray()
        #print "C1" , len(b) ,b
        out_.clear()
        m[0].key_type = self.TYPE_STRING1
        m[0].val_type = self.TYPE_SIMPLE_LIST
        m[0].key = tozjj(mapKey,"str",0)
        m[0].val = b
        #print "m[0].key ",m[0].key
        out_.WriteMap(m, 0)
        b = out_.toByteArray()
        #print "C3" , len( b ) , b
        out_.clear()
        req.iversion = iversion
        req.iRequestId = iRequestId
        req.sServantName = sServantName
        req.sFuncName = sFuncName
        req.sBuffer = b
        req.context = []
        req.status = []
        self.Write_RequestPacket(out_, req)
        b = out_.toByteArray()
        pk.Empty()
        pk.SetInt(len(b) + 4)
        pk.SetBin(b)
        #print "CC" ,len(pk.GetAll( )), pk.GetAll( )
        return(pk.GetAll())

    def Pack_Login(self):
        pk = _pack();b = [];tmp = [];wupbuffer = []
        tlv109 = [];tlv124 = [];tlv128 = [];tlv16e = [];
        self.qq.shareKey = tozjj("957C3AAFBF6FAF1D2C2F19A5EA04E51C")
        self.qq.pub_key = tozjj("02244B79F2239755E73C73FF583D4EC5625C19BF8095446DE1")
        # print "key",self.qq.shareKey,self.qq.pub_key
        # self.qq.TGTKey = Xbin.GetRandomBin(16)
        self.qq.TGTKey = [0 for i in range(16)]
        # self.qq.tim = Xbin.flip(tozjj(int(time.time()),"int"))
        self.qq.tim = [86, 247, 21, 166]
        # self.qq.randKey = Xbin.GetRandomBin(16)
        self.qq.randKey = [0 for i in range(16)]
        # print "TGTKey",self.qq.TGTKey
        # print self.qq.tim
        # print "randKey",self.qq.randKey
        
        pk.Empty()
        pk.SetHex("00 09")
        pk.SetShort(19)        # 00 13 //下面tlv个数
        
        pk.SetBin(self.tlv.tlv18(self.qq.user))
        pk.SetBin(self.tlv.tlv1(self.qq.user, self.qq.tim))
        pk.SetBin(self.tlv.tlv106(self.qq.user, self.qq.md51, self.qq.md52, self.qq.TGTKey, self.gb.imei_, self.qq.tim, self.gb.appId))
        pk.SetBin(self.tlv.tlv116())
        pk.SetBin(self.tlv.tlv100(self.gb.appId))
        pk.SetBin(self.tlv.tlv107())
        pk.SetBin(self.tlv.tlv108(self.qq._ksid))
        self.qq._ksid = []
        
        tlv109 = self.tlv.tlv109(self.gb.imei_)
        tlv124 = self.tlv.tlv124(self.gb.os_type, self.gb.os_version, self.gb._network_type, self.gb._apn)
        tlv128 = self.tlv.tlv128(self.gb.device, self.gb.imei_)
        tlv16e = self.tlv.tlv16e(self.gb.device)
        # print "tlv16e",tlv16e,self.gb.device
        # print "test",self.qq.TGTKey, tlv109, tlv124, tlv128, tlv16e
        pk.SetBin(self.tlv.tlv144(self.qq.TGTKey, tlv109, tlv124, tlv128, tlv16e))
        # print "all",pk.GetAll()
        pk.SetBin(self.tlv.tlv142(self.gb._apk_id))
        pk.SetBin(self.tlv.tlv145(self.gb.imei_))
        pk.SetBin(self.tlv.tlv154(self.RequestId))
        pk.SetBin(self.tlv.tlv141(self.gb._network_type, self.gb._apn))
        pk.SetBin(self.tlv.tlv8())
        pk.SetBin(self.tlv.tlv16b())
        pk.SetBin(self.tlv.tlv147(self.gb._apk_v, self.gb._apk_sig))
        pk.SetBin(self.tlv.tlv177())
        pk.SetBin(self.tlv.tlv187())
        pk.SetBin(self.tlv.tlv188())
        pk.SetBin(self.tlv.tlv191())
        wupbuffer = pk.GetAll()
        # print "wupbuffe1r",wupbuffer
        wupbuffer = self.Pack_Pc("0810",Hash.QQTEA(wupbuffer, self.qq.shareKey),self.qq.randKey, self.qq.pub_key)
        # print "wupbuffer",wupbuffer
        # print "ksid",self.qq._ksid
        t = self.Make_login_sendSsoMsg("wtlogin.login",wupbuffer,[],self.gb.imei,self.qq._ksid,self.gb.ver,1)
        # print "t",t
        return t

    def Pack_OidbSvc_0x7a2_0(self):    # OidbSvc_0x7a2_0
        b = tozjj("08 A2 0F 10 00 18 00 22 02 08 00")
        # print "bin",b
        #print "OidbSvc.0x7a2_0",b,self.qq.Token004C,self.gb.imei,self.qq._ksid,self.gb.ver
        return(self.Make_login_sendSsoMsg("OidbSvc.0x7a2_0",b,self.qq.Token004C,self.gb.imei,self.qq._ksid,self.gb.ver,0))
    def Pack_Pc(self,cmd,b,ext_key = [],ext_bin = []):
        # print "b",b
        pk = _pack()
        ext_bin_null = 0
        tmp = []
        pk.Empty()
        pk.SetHex(self.gb.pc_ver)
        pk.SetHex(cmd)
        pk.SetShort(self.getSubCmd())
        pk.SetBin(self.qq.user)
        pk.SetHex("03 07 00 00 00 00 02 00 00 00 00 00 00 00 00")
        if(ext_bin != [] and len(ext_bin)>0):
            ext_bin_null = 0
            pk.SetHex("01 01")
        else:
            ext_bin_null = 1
            pk.SetHex("01 02")
        # print "ext_key",ext_key
        pk.SetBin(ext_key)
        pk.SetHex("01 02")
        pk.SetShort(len(ext_bin))
        if(ext_bin_null == 1):
            pk.SetHex("00 00")
        else:
            pk.SetBin(ext_bin)
        pk.SetBin(b)
        pk.SetHex("03")
        tmp = pk.GetAll()
        pk.Empty()
        pk.SetHex("02")
        pk.SetShort(len(tmp) + 3)
        pk.SetBin(tmp)
        tmp =  pk.GetAll()
        # print tmp
        return(tmp)

    def Pack_StatSvc_get(self):        # 心跳StatSvc_get
        out_ = JceOutputStream();b = []
        out_.WriteInt(self.qq.QQ, 0)
        out_.WriteByte(7, 1)
        out_.WriteStringByte("", 2)
        out_.WriteByte(11, 3)
        out_.WriteByte(0, 4)
        out_.WriteByte(0, 5)
        out_.WriteByte(0, 6)
        out_.WriteByte(0, 7)
        out_.WriteByte(0, 8)
        out_.WriteByte(0, 9)
        out_.WriteByte(0, 10)
        out_.WriteByte(0, 11)
        
        b = out_.toByteArray()
        return(self.Make_sendSsoMsg_simple("StatSvc.get", 3, 1819559151, "PushService", "SvcReqGet", "SvcReqGet", b))
    def Pack_StatSvc_Register(self,lBid,iStatus,timeStamp):   # StatSvc_Register
        # lbid    7上线 0下线
        # istatus    11上线 21下线
        # timestamp     0 上 5下
        req = dt.JceStruct_RequestPacket()
        out_ = JceOutputStream()
        m = [dt.JceMap()]
        b = []
        struct_ = dt.JceStruct_SvcReqRegister()
        struct_.lUin = self.qq.QQ
        struct_.lBid = lBid
        struct_.iStatus = iStatus
        struct_.timeStamp = timeStamp
        struct_._11 = 15
        struct_._12 = 1
        struct_._imei_ = self.gb.imei_
        struct_._17 = 2052
        struct_._19_device = self.gb.device
        struct_._20_device = self.gb.device
        struct_._21_sys_ver = self.gb.os_version
        #print "struct",struct_.lUin, struct_.lBid, struct_.iStatus, struct_.timeStamp, struct_._imei_, struct_._19_device, struct_._21_sys_ver
        # print "out1",out_.toByteArray()
        self.Write_SvcReqRegister(out_, struct_)
        # print "out2",out_.toByteArray()
        b = out_.toByteArray()
        # b = [3, 167L, 140L, 63L, 133L, 16, 7, 44, 54, 0, 64, 11, 92, 108, 124, 140, 156, 172, 176, 15, 192, 1, 214, 0, 236, 253, 16, 0, 0, 15, 56, 54, 54, 56, 49, 57, 48, 50, 55, 50, 51, 54, 54, 53, 56, 241, 17, 8, 4, 252, 18, 246, 19, 0, 246, 20, 0, 246, 21, 0]
        # print "b111",b
        out_.clear()
        #print "out1",len(out_.toByteArray()),out_.toByteArray()
        out_.WriteJceStruct(b, 0)
        #print "out2",len(out_.toByteArray()),out_.toByteArray()
        b =  out_.toByteArray()
        # print "b",b
        out_.clear()
        #print "out3",len(out_.toByteArray()),out_.toByteArray()
        m[0].key_type = self.TYPE_STRING1
        m[0].val_type = self.TYPE_SIMPLE_LIST
        m[0].key = tozjj("SvcReqRegister","str")
        m[0].val = b
        out_.WriteMap(m, 0)
        #print "out4",len(out_.toByteArray()),out_.toByteArray()
        b =  out_.toByteArray()
        # print "b",b
        out_.clear()
        #print "out5",len(out_.toByteArray()),out_.toByteArray()
        req.iversion = 3
        req.sServantName = "PushService"
        req.sFuncName = "SvcReqRegister"
        req.sBuffer = b
        req.context = []
        req.status = []
        self.Write_RequestPacket(out_, req)
        #print "out6",len(out_.toByteArray()),out_.toByteArray()
        b = out_.toByteArray()
        #print "b",b
        # self.qq.Token004C = [122, 81, 177, 2, 160, 52, 10, 53, 94, 193, 226, 243, 92, 94, 168, 39, 118, 114, 8, 119, 207, 3, 239, 150, 124, 85, 10, 59, 157, 37, 180, 76, 131, 138, 224, 25, 147, 193, 52, 18, 63, 239, 88, 54, 44, 134, 72, 161, 108, 200, 193, 183, 164, 4, 12, 200, 27, 92, 102, 109, 0, 52, 22, 167, 140, 9, 218, 189, 251, 164, 52, 157]
        # self.qq.Token002C = [165L, 197L, 58L, 249L, 249L, 26L, 6L, 221L, 79L, 204L, 24L, 206L, 90L, 144L, 38L, 97L, 247L, 238L, 93L, 39L, 98L, 178L, 48L, 170L, 16L, 93L, 51L, 91L, 189L, 177L, 201L, 4L, 13L, 217L, 158L, 93L, 92L, 125L, 3L, 202L, 47L, 126L, 16L, 77L, 143L, 143L, 193L, 51L, 90L, 199L, 151L, 39L, 192L, 196L, 18L, 71L, 190L, 23L, 245L, 136L, 12L, 47L, 9L, 111L]
        t = self.Make_login_sendSsoMsg("StatSvc.register", b, self.qq.Token004C, self.gb.imei, self.qq._ksid, self.gb.ver, 0)
        # print "mmm",len(t),t
        return(t)
        
    def Pack_StatSvc_Register_offonline(self): # 下线
        return self.Pack_StatSvc_Register(0, 21, 5)
    def Pack_StatSvc_Register_online(self):    # 上线
        return self.Pack_StatSvc_Register(7, 11, 0)
    def Pack_VieryImage(self,code):    # 构造发送验证码包
        pk = _pack()
        wupbuffer = []
        pk.Empty()
        pk.SetHex("00 02 00 ")
        pk.SetByte(4)  #  count
        pk.SetBin(self.tlv.tlv2(code, self.qq.VieryToken1))
        # print self.qq.VieryToken1,code
        pk.SetBin(self.tlv.tlv8())
        pk.SetBin(self.tlv.tlv104(self.qq.VieryToken2))
        # print self.qq.VieryToken2
        pk.SetBin(self.tlv.tlv116())
        wupbuffer = pk.GetAll()
        wupbuffer = self.Pack_Pc("0810", Hash.QQTEA(wupbuffer, self.qq.shareKey), self.qq.randKey, self.qq.pub_key)
        t = self.Make_login_sendSsoMsg("wtlogin.login", wupbuffer, [], self.gb.imei, self.qq._ksid, self.gb.ver, 1)
        # print "t",len(t),t
        return t
    def QQ_offline(self):      # 下线
        self.Fun_send(self.Pack_StatSvc_Register_offonline(), 3000)
    def QQ_online(self):
        b = []
        b = self.Fun_send(self.Pack_OidbSvc_0x7a2_0(),3000)
        #print "b",b
        self.Fun_recv(b)
        b = self.Fun_send(self.Pack_StatSvc_Register_online(), 3000)
        self.Fun_recv(b)
        if(len(b) <= 0):
            print "二次登录数据失效或QQ号冻结，请检查或重新取二次登录数据"
        else:
            print "登陆完成"
            # 启动线程(&循环处理消息, , )
    def QQ_getfriendlist(self):
        self.m_friends = [dt.JceStruct_FriendInfo()]
        self.Fun_SendGetFriendList (0, 20)
    def QQ_loadTokenData(self,Token002C=[],Token004C=[],sessionKey=[]):
        #Token002C = tozjj("A4 81 A2 75 30 A2 B0 CF AC 80 DA D8 A1 26 69 61 47 92 E6 0D 8A E0 B2 AF 1B 4C 29 8B 0F 7F DD B4 A5 A9 11 A9 8B 96 B8 A9 13 E1 D0 43 31 91 20 E0 DA EB DA 79 A4 82 04 40 83 62 C5 0E 98 FC A4 AA" )
        #Token004C = tozjj("F2 3E 05 B6 70 28 E4 AE 04 8D EA 2C 08 07 A9 D1 5D BB 0B DA A5 4F A9 00 34 A3 9C C1 D0 23 88 79 FA 5C E0 4E 02 5C 08 40 FE F2 19 88 2C DD 0C 4C 30 83 B1 51 33 28 74 F7 C9 12 E8 54 04 1C 8A 8E 53 E1 2C F6 2B A8 AF A4")
        #sessionKey = tozjj( "21 74 62 62 60 27 67 69 59 75 5F 56 3C 6D 7D 69 " )
        self.qq.Token002C = Token002C
        self.qq.Token004C = Token004C
        self.qq.sessionKey = sessionKey
        self.qq.key = sessionKey
    def QQ_sendfriendmsg(self,qqnum,msg):# 发好友消息
        self.Fun_send(self.Pack_MessageSvc_offlinemsg(long(qqnum),msg))
    def QQ_sendgroupmsg(self,num,msg):
        self.Fun_send(self.Pack_MessageSvc_SendGroupMsg(num,msg))
    def QQ_xintiao(self):      # QQ_心跳
        self.Fun_send(self.Pack_StatSvc_get())
    def unPack_has_len(self,serviceCmd,bin):
        return bin
    def Un_pack(self,b = [],bl = 0):
        pos1 = 0
        pos1 = findlist(b,self.qq.caption)
        b = b[(len(b)-(len(b)-pos1-len(self.qq.caption)+1)) :]
        if(bl == 1):
            pos1 = findlist(b,self.qq.caption)
            b = b[(len(b)-(len(b)-pos1-len(self.qq.caption)+1)) :]
        return b
    def Un_Pack_ErrMsg(self,b):
        title = "";message = "";typ = 0;unPack = _unpack();
        unPack.SetData(b)
        unPack.GetShort()
        unPack.GetByte()
        unPack.GetInt()
        unPack.GetShort()
        typ = unPack.GetInt()
        title = list2str(unPack.GetBin(unPack.GetShort())+[0])
        message = list2str(unPack.GetBin(unPack.GetShort())+[0])
        self.last_error = title+":"+message
        #print "Un_Pack_ErrMsg",self.last_error
    def Un_Pack_OnlinePush_PbPushGroupMsg(self,b):#OnlinePush_PbPushGroupMsg
        return b
    def Un_Pack_Login(self,b = []):
        l = 0;unPack = _unpack();_0030 = [];
        b = self.Un_Pack_Login_Pc(b)
        if(len(b) == 0):
            return 0
        unPack.SetData(b)
        unPack.GetShort()
        unPack.GetByte()
        unPack.GetInt()
        l = unPack.GetShort()
        b = unPack.GetBin(l)
        
        b = Hash.UNQQTEA(b, self.qq.TGTKey)
        
        self.Un_Tlv(b)
        
        self.qq.key = self.qq.sessionKey;
        
        # print "sessionkey:",self.qq.sessionkey
        # print "skey:",self.qq.skey
        # print "sid:",self.qq.sid
        # print "stweb:",self.qq.stweb
        # print "vkey:",self.qq.vkey
        
        self.qq.loginState = self.login_state_success
        return 1

    def Un_Pack_Login_Pc(self,b = []):   # 只有登陆时用
        unPack = _unpack();l = 0;result = 0;
        unPack.SetData(b)
        l = unPack.GetInt()
        b = unPack.GetAll()
        
        unPack.SetData(b)
        unPack.GetByte()
        l = unPack.GetShort()
        unPack.GetBin(10)  # 1F 41 08 10 00 01 18 B4 A1 BC
        unPack.GetBin(2)
        result = unPack.GetByte()
        
        b = unPack.GetBin(l- 16 - 1)
        b = Hash.UNQQTEA(b,self.qq.shareKey)
        if(result != 0):
            #print "result",result
            if(result == 2):# 
                # print "yzm",b
                self.Un_Pack_VieryImage(b)
                self.last_error = "需要输入验证码"
                self.qq.loginState = self.login_state_veriy
                return []
            self.Un_Pack_ErrMsg(b)
            b = []
            self.qq.loginState = self.login_state_logining
        return b
    def Un_Pack_RequestPacket(self,b,CardData):
        req = dt.JceStruct_RequestPacket()
        in_ = JceInputStream()
        in_.wrap(b)
        self.Read_RequestPacket(in_, req)
        if(len(req.sBuffer) == 0):
            return
        in_.wrap(req.sBuffer)
        self.Un_Pack_Map(in_,CardData)
    def Un_Pack_Map(self,in_,CardData):
        t_friendListResp = dt.JceStruct_FriendListResp()
        t_type = 0;t_count = 0;i = 0;t_key = "";t_bin = [];
        t_is_firends_req = 0;t_is_groups_req = 0;j_count = 0;
        j = 0;t_verify_type = 0;question = "";friendUin = 0;
        t_suc = 0;t_msg = "";
        
        t_type = in_.ReadType()
        if(t_type != self.TYPE_MAP):
            return
        t_count = in_.ReadShort(0)
        for i in range(t_count):
            t_key = in_.ReadString(0)
            #print t_key
            if(t_key == "FLRESP"):        #  所有好友列表
                t_bin = in_.ReadSimpleList(1)
                self.Read_FLRESP(t_bin, t_friendListResp, self.m_friends)
                t_is_firends_req = 1
            elif(t_key == "FSRESP"):      # 加好请求设置信息返回
                t_bin = in_.ReadSimpleList(1)
                t_verify_type, question, friendUin = self.Read_FSRESP(t_bin, t_verify_type, question, friendUin)
                # QQ_事件_加好友获取设置返回(self.qq.QQ, friendUin, t_verify_type, question)
            elif(t_key == "RespGetEncounterV2"):
                t_type = in_.ReadType()
                if(t_type == self.TYPE_MAP):
                    j_count = in_.ReadShort(0)
                    for i in range(j_count):
                        t_key = in_.ReadString(0)
                        t_bin = in_.ReadSimpleList(1)
                        if(t_key == "EncounterSvc.RespGetEncounterV2"):
                            t_key = self.Read_EncounterSvc_RespGetEncounterV2(t_bin, t_key)
                            #  可以做继续获取。
                            # QQ_事件_附近人_获取完毕(self.qq.QQ)
            elif(t_key == "GetTroopListRespV2"):
                t_bin = in_.ReadSimpleList(1)
                self.Read_GroupMngRes2(t_bin)
            elif(t_key == "GTMLRESP"):
                t_bin = in_.ReadSimpleList(1)
                self.Read_GroupMemberList(t_bin)
            elif(t_key == "RespHeader"):
                t_bin = in_.ReadSimpleList(1)
            elif(t_key == "FSOLRESP"):
                t_bin = in_.ReadSimpleList(1)
                self.Read_onlinefriendList(t_bin)
            elif(t_key == "GAIRESP"):     #  获取自动分组
                t_bin = in_.ReadSimpleList(1)
            elif(t_key == "AFRESP"):
                t_bin = in_.ReadSimpleList(1)
                t_suc, t_msg = self.Read_AFRESP(t_bin, t_suc, t_msg)
                # QQ_事件_加好友结果返回( q.QQ, t_suc, t_msg)
            elif(t_key == "GroupMngRes"):
                t_type = in_.ReadType()
                if(t_type == self.TYPE_MAP):
                    j_count = in_.ReadShort(0)
                    for j in range(j_count):
                        t_key = in_.ReadString(0)
                        t_bin = in_.ReadSimpleList(1)
                        if(t_key == "KQQ.GroupMngRes"):
                            self.Read_GroupMngRes(t_bin)
            elif(t_key == "req_PushNotify"):
                t_type = in_.ReadType()
                if(t_type == self.TYPE_MAP):
                    j_count = in_.ReadShort(0)
                    for j in range(j_count):
                        t_key = in_.ReadString(0)
                        t_bin = in_.ReadSimpleList(1)
                        if(t_key == "PushNotifyPack.RequestPushNotify"):
                            # print tkey,tohex(t_bin)
                            pass
            elif(t_key == "req"):
                t_type = in_.ReadType()
                if(t_type == self.TYPE_MAP):
                    j_count = in_.ReadShort(0)
                    for j in range(j_count):
                        t_key = in_.ReadString(0)
                        t_bin = in_.ReadSimpleList(1)
                        if(t_key == "PushNotifyPack.SvcRequestPushReadedNotify"):
                            # print tkey,tohex(t_bin)
                            pass
            elif(t_key == "RespHead"):            #  查看名片返回
                t_type = in_.ReadType()
                if(t_type == self.TYPE_MAP):
                    j_count = in_.ReadShort(0)
                    for j in range(j_count):
                        t_key = in_.ReadString(0)
                        t_bin = in_.ReadSimpleList(1)
                        if(t_key == "SummaryCard.RespHead"):
                            pass
            elif(t_key == "RespSummaryCard"):     #  查看名片返回
                t_type = in_.ReadType()
                if(t_type == self.TYPE_MAP):
                    j_count = in_.ReadShort(0)
                    for j in range(j_count):
                        t_key = in_.ReadString(0)
                        t_bin = in_.ReadSimpleList(1)
                        if(t_key == "SummaryCard.RespSummaryCard"):
                            pass
            elif(t_key == "rsp"):     #  查看名片返回
                t_type = in_.ReadType()
                if(t_type == self.TYPE_MAP):
                    j_count = in_.ReadShort(0)
                    for j in range(j_count):
                        t_key = in_.ReadString(0)
                        t_bin = in_.ReadSimpleList(1)
                        if(t_key == "summary_card.SSummaryCardRsp"):
                            pass
            else:
                print "未处理 key",t_key
            if(t_is_firends_req == 1):
                print "获取好友列表中,请稍候!"
                # print "好友 == 》 获取位置 = ",t_friendListResp.startIndex,"  准备获取数 = ",t_friendListResp.getfriendCount,"  总共 = ",t_friendListResp.totoal_friend_count),"  获取数 = ",t_friendListResp.friend_count 
                if(t_friendListResp.startIndex + t_friendListResp.getfriendCount<t_friendListResp.totoal_friend_count):
                    self.Fun_SendGetFriendList(t_friendListResp.startIndex + t_friendListResp.getfriendCount, 20)
                else:
                    print "好友 == 》 获取完毕，总共 = ",len(self.m_friends)
                    # QQ_事件_好友获取完毕(self.qq.QQ)

        
    def Un_Pack_VieryImage(self,b):
        Unpack = _unpack();i = 0;
        Unpack.SetData(b)
        Unpack.GetBin(3)
        self.Un_Tlv(Unpack.GetAll())
    def Un_Tlv(self,b):
        unPack = _unpack();
        tlv_count = 0;tlv_cmd = [];tlv_len = 0;
        unPack.SetData(b)
        tlv_count = unPack.GetShort()
        for i in range(tlv_count):
            tlv_cmd = unPack.GetBin(2)
            tlv_len = unPack.GetShort()
            self.tlv_get((Xbin.Bin2Hex(tlv_cmd)), unPack.GetBin(tlv_len))
    def tlv_get(self,tlv_cmd,b):
        unPack = _unpack();
        l = 0;face = 0;age = 0;gander = 0;i = 0
        falg = 0;tim = 0;ip = "";
        unPack.SetData(b)
        # print "tlv_cmd",tlv_cmd
        a = tlv_cmd
        a = [a[0]+a[1],a[2]+a[3]]
        tlv_cmd = a
        if(tlv_cmd == ["01","6A"]):
            pass
        elif(tlv_cmd == ["01","06"]):
            pass
        elif(tlv_cmd == ["01","0C"]):
            pass
        elif(tlv_cmd == ["01","0A"]):
            self.qq.Token004C = b
        elif(tlv_cmd == ["01","0D"]):
            pass
        elif(tlv_cmd == ["01","14"]):
            self.qq.Token0058 = self.tlv.tlv114_get0058(b)
        elif(tlv_cmd == ["01","0E"]):
            self.qq.mST1Key = b
        elif(tlv_cmd == ["01","03"]):
            self.qq.stweb = tohex(b)
        elif(tlv_cmd == ["01","1F"]):
            pass
        elif(tlv_cmd == ["01","38"]):
            l = unPack.GetInt()
            for i in range(l):
                flag = unPack.GetShort()
                tim = unPack.GetInt()
                unPack.GetInt()
        elif(tlv_cmd == ["01","1A"]):  # 昵称
            face = unPack.GetShort()
            age = unPack.GetByte()
            gander = unPack.GetByte()
            l = unPack.GetByte()
            # l = unPack.GetByte()
            self.qq.nick = list2str((unPack.GetBin(l))).decode("u8")
            print "昵称",self.qq.nick,"face：",face,"age:",age,"gander：",gander
        elif(tlv_cmd == ["01","20"]):
            self.qq.skey = b
        elif(tlv_cmd == ["01","36"]):
            self.qq.vkey = b
        elif(tlv_cmd == ["01","1A"]):
            pass
        elif(tlv_cmd == ["01","20"]):
            pass
        elif(tlv_cmd == ["01","36"]):
            pass
        elif(tlv_cmd == ["03","05"]):
            self.qq.sessionKey = b
        elif(tlv_cmd == ["01","43"]):
            self.qq.Token002C = b
        elif(tlv_cmd == ["01","64"]):
            self.qq.sid = b
        elif(tlv_cmd == ["01","18"]):
            pass
        elif(tlv_cmd == ["01","63"]):
            pass
        elif(tlv_cmd == ["01","30"]):
            unPack.GetShort()
            tim = unPack.GetInt()
            ip = unPack.GetBin(4)
            ip = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
            print "time:",tim,"ip:",ip
        elif(tlv_cmd == ["01","05"]):
            # print "0105"
            l = unPack.GetShort()
            self.qq.VieryToken1 = unPack.GetBin(l)
            l = unPack.GetShort()
            self.qq.Viery = unPack.GetBin(l)
            # print self.qq.Viery
            
        elif(tlv_cmd == ["01","04"]):
            self.qq.VieryToken2 = b
        elif(tlv_cmd == ["01","65"]):    # 需要输入验证码原因
                                       # 请输入图中字符，帮助我们完成安全测试
            pass
        elif(tlv_cmd == ["01","08"]):    # ksid
            pass
        elif(tlv_cmd == ["01","6D"]):
            self.qq.superkey = b
        elif(tlv_cmd == ["01","6C"]):
            self.qq.pskey = b
        else:
            print "Unknown tlv_cmd",tlv_cmd# ,list2str(b)
    def getViery(self):
        # open("vpic.jpg","wb").write(tohex(self.qq.yzm))
        return list2str(self.qq.Viery)
    def increase_ssoSeq(self):
        if(self.RequestId>2147483647):
            self.RequestId = 10000
        else:
            self.RequestId += 1
    def Fun_send(self,b,wait = ""):
        suc = 0
        self.increase_ssoSeq()
        self.tcp("send",b)
        if(wait == ""):return []
        b = self.tcp("rec")
        return b
    def Fun_SendCode(self,code):
        b = []
        b = self.Fun_send(self.Pack_VieryImage(code), 3000)
        self.Fun_recv(b)
        return self.qq.loginState
    def Fun_recv(self,data = []):
        b = [];bl = 0;test = [];unPack = _unpack();sso_seq = 0;
        l = 0;serviceCmd = "";head_len = 0;body_bin = [];
        if(len(data) == 0):return
        # 一次性把包收完
        b = self.Un_pack(data)
        # 大于一定长度之和会分包发送，要自己处理下哦
        b = Hash.UNQQTEA(b,self.qq.key)
        l = len(b)
        unPack.SetData(b)
        
        head_len = unPack.GetInt()
        b = unPack.GetBin(head_len-4)         # 上面包内容
        body_bin = unPack.GetAll()
        
        unPack.SetData(b)
        sso_seq = unPack.GetInt()
        if(unPack.GetBin(4) == [0,0,0,0]):
            unPack.GetBin(4)
        else:
            unPack.GetBin(unPack.GetInt()-4)
        
        serviceCmd = list2str(unPack.GetBin(unPack.GetInt()-4))
        # print "self.qq.loginState 1",self.qq.loginState,serviceCmd
        if(serviceCmd == "wtlogin.login"):
            #print "upk"
            self.Un_Pack_Login(body_bin)
        else:
            self.Fun_msg_Handle(sso_seq,serviceCmd,body_bin)
        # print "self.qq.loginState 2",self.qq.loginState
    def Fun_Keep(self):
        wait=5000;suc=0;l=0;unPack=_unpack();b=[];req=_pack()
        for i in range(20):    #避免死循环
            b=self.tcp("rec",wait)
            if(len(b) == 0):continue
            self.m_bin = self.m_bin + b
            unPack.SetData(self.m_bin)

            while(unPack.Len() >= 4):
                l = unPack.GetInt()
                if(l <= unPack.Len() + 4):
                    b = unPack.GetBin( len - 4)
                    self.Fun_recv(b)
                    self.m_bin = unPack.GetAll()
                    unPack.SetData(self.m_bin)
                else:
                    req.Empty()
                    req.SetInt(l)
                    req.SetBin(unPack.GetAll())
                    unPack.SetData(req.GetAll())
                    unPack.SetData(req.GetAll())
                    break

    def Fun_msg_Handle(self,sso_seq_,serviceCmd,b):    # # # 以上是登陆
        unPack = _unpack()
        l = 0;
        t_b = []
        app_str = ""
        
        unPack.SetData(b)
        l  ==  unPack.GetInt()
        b  ==  unPack.GetBin(l)
        if(serviceCmd  ==  "OidbSvc.0x7a2_0"):
            pass
        elif(serviceCmd  ==  "friendlist.getFriendGroupList"):
            self.Un_Pack_RequestPacket(b)
        elif(serviceCmd  ==  "EncounterSvc.ReqGetEncounter"):
            t_b  ==  inflate_Decompress(b)  #  解压
            # 置剪辑板文本(字节集到十六进制文本(t_b))
            self.Un_Pack_RequestPacket(t_b)
        elif(serviceCmd  ==  "friendlist.getUserAddFriendSetting"):
            self.Un_Pack_RequestPacket(b)
        elif(serviceCmd  ==  "SummaryCard.ReqCondSearch"):
            self.Read_people(b)
        elif(serviceCmd  ==  "friendlist.GetAutoInfoReq"):
            self.Un_Pack_RequestPacket(b)
        elif(serviceCmd  ==  "SQQzoneSvc.getMainPage"):
            #  调试输出("SQQzoneSvc.getMainPage", 字节集到十六进制文本(b))
            self.Read_MainPage_rq(b)
        elif(serviceCmd  ==  "friendlist.addFriend"):
            self.Un_Pack_RequestPacket(b)
        elif(serviceCmd  ==  "ProfileService.GroupMngReq"):
            self.Un_Pack_RequestPacket(b)
        elif(serviceCmd  ==  "OnlinePush.PbPushGroupMsg"):
            self.Un_Pack_OnlinePush_PbPushGroupMsg(b)
        elif(serviceCmd  ==  "MessageSvc.PushReaded"):  #  如果电脑或者网页上已经看了 会发送此消息
            self.unPack_has_len(serviceCmd, b)
        elif(serviceCmd  ==  "MessageSvc.PushNotify"):  #  来消息通知
            self.unPack_has_len(serviceCmd, b)
        elif(serviceCmd  ==  "StatSvc.get"):
            print "心跳",time.time()
        elif(serviceCmd  ==  "SummaryCard.ReqSummaryCard"):
            print tohex(b)
            if(tohex(b).find("78DA") == -1):
                self.Un_Pack_RequestPacket(b)
            else:
                b  = inflate_Decompress(b)
                self.Un_Pack_RequestPacket(b)
        elif(serviceCmd  ==  "ConfigPushSvc.PushReq"):
            pass
        elif(serviceCmd  ==  "OidbSvc.0x4ff_9"):
            print "修改昵称完成"
        elif(serviceCmd  ==  "QQServiceDiscussSvc.ReqGetDiscuss"):
            self.Read_RespGetDiscuss(b)
        elif(serviceCmd  ==  "account.RequestReBindMobile"):
            print "已发送验证码到手机"
        elif(serviceCmd  ==  "Signature.auth"):
            print "发表签名成功"
        elif(serviceCmd  ==  "SQQzoneSvc.publishmess"):
            print "留言成功"
        elif(serviceCmd  ==  "VisitorSvc.ReqFavorite"):
            print "赞名片成功"
        elif(serviceCmd  ==  "friendlist.GetSimpleOnlineFriendInfoReq"):
            if(tohex(b).find("78DA") == -1):
                self.Un_Pack_RequestPacket(b)
            else:
                b  ==  inflate_Decompress(b)
                self.Un_Pack_RequestPacket(b)
        elif(serviceCmd  ==  "FriendList.GetTroopListReqV2"):
            print tohex(b)
            if(tohex(b)[:4] == "78DA"):
                b  ==  inflate_Decompress(b)
                self.Un_Pack_RequestPacket(b)
            else:
                self.Un_Pack_RequestPacket(b)
        elif(serviceCmd  ==  "friendlist.getTroopMemberList"):
            if(tohex(b).find("78DA") == -1):
                print tohex(b)
                self.Un_Pack_RequestPacket(b)
            else:
                b = inflate_Decompress(b)
                self.Un_Pack_RequestPacket(b)
        elif(serviceCmd  ==  "QQServiceDiscussSvc.ReqCreateDiscuss"):
            self.Read_DiscussRespHeader(b)
        elif(serviceCmd  ==  "QQServiceDiscussSvc.ReqAddDiscussMember"):
            self.Read_ReqAddDiscussMember(b)
        elif(serviceCmd  ==  "SQQzoneSvc.getApplist"):
            print " ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  == SQQzoneSvc.getApplist ==  ==  ==  ==  ==  ==  ==  ==  ==  == ", tohex(b)
            appstr = binmid(tohex(b),"73745D0001","6D000100")
            appstr = appstr[4:]
            if(len(appstr) != 0):
                b = inflate_Decompress(tozjj(appstr))
            else:
                print "目标设置了访问权限！"
            self.Read_applist(b)
        else:
            print "未处理消息"# ,serviceCmd,tohex(b)
            return
        if(unPack.Len()>0):
            print "消息未处理完"# ,serviceCmd,list2str(unPack.GetAll())
    def Fun_SendGetFriendList(self,startIndex,getfriendCount):
        self.Fun_send(self.Pack_friendlist_getFriendGroupList(getfriendCount, startIndex))
    def Fun_again_Login(self):
        m_b=[]
        self.qq.loginState = self.login_state_logining
        if(self.tcp("connect") == 0):
            print "无法连接服务器"
            return self.qq.loginState
        self.QQ_online()
        #启动线程 (&循环处理消息, , thread_hwnd)
        return self.qq.loginState
    def Fun_Login(self):
        b = []
        self.tcp("disconnect")
        self.qq.loginState = self.login_state_logining
        if(self.tcp("connect") == 0):
            print "无法连接服务器"
            return self.qq.loginState
        b = self.Fun_send(self.Pack_Login(),3000)
        if(b == []):
            self.last_error = "登陆返回包为空"
            return self.qq.loginState
        self.Fun_recv(b)
        return self.qq.loginState
class Tlv_:
    def __init__(self):
        pass
    def tlv_pk(self,cmd,b):
        pk = _pack()
        pk.Empty()
        pk.SetHex(cmd)
        pk.SetShort(len(b))
        pk.SetBin(b)
        return(pk.GetAll())
    def tlv18(self,user):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00 01")
        pk.SetHex("00 00 06 00")
        pk.SetHex("00 00 00 10")
        pk.SetHex("00 00 00 00")
        pk.SetBin(user)
        pk.SetHex("00 00")
        pk.SetHex("00 00")
        return(self.tlv_pk("00 18", pk.GetAll()))
    def tlv1(self,user,tim):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00 01")
        # pk.SetBin(Xbin.GetRandomBin(4))
        pk.SetBin([0,0,0,0])
        pk.SetBin(user)
        pk.SetBin(tim)
        pk.SetHex("00 00 00 00")
        pk.SetHex("00 00")
        return(self.tlv_pk("00 01", pk.GetAll()))
    def tlv2(self,code,VieryToken1):
        pk = _pack()
        pk.Empty()
        pk.SetInt(len(code))
        pk.SetBin(tozjj(code,"str"))
        pk.SetShort(len(VieryToken1))
        pk.SetBin(VieryToken1)
        return(self.tlv_pk("00 02", pk.GetAll()))
    def tlv106(self,user,md5pass,md52pass,_TGTKey,imei_,tim,appId):
        pk = _pack()
        pk.SetHex("00 03")
        # pk.SetBin(Xbin.GetRandomBin(4))
        pk.SetBin([0,0,0,0])
        pk.SetHex("00 00 00 05")
        pk.SetHex("00 00 00 10")
        pk.SetHex("00 00 00 00")
        pk.SetHex("00 00 00 00")
        pk.SetBin(user)
        pk.SetBin(tim)
        pk.SetHex("00 00 00 00 01")
        pk.SetBin(md5pass)
        pk.SetBin(_TGTKey)
        pk.SetHex("00 00 00 00")
        pk.SetHex("01")
        pk.SetBin(imei_)
        pk.SetInt(appId)
        pk.SetHex("00 00 00 01")
        pk.SetHex("00 00")
        return(self.tlv_pk("01 06", Hash.QQTEA(pk.GetAll(), md52pass)))
    def tlv116(self):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00")
        pk.SetHex("00 00 7F 7C")
        pk.SetHex("00 01 04 00")
        pk.SetHex("00")
        return(self.tlv_pk("01 16", pk.GetAll()))
    def tlv100(self,appId):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00 01")
        pk.SetHex("00 00 00 05")
        pk.SetHex("00 00 00 10")
        pk.SetInt(appId)
        pk.SetHex("00 00 00 00")
        pk.SetHex("00 0E 10 E0")
        return(self.tlv_pk("01 00", pk.GetAll()))
    def tlv104(self,VieryToken2):
        pk = _pack()
        pk.Empty()
        pk.SetBin(VieryToken2)
        return(self.tlv_pk("01 04", pk.GetAll()))
    def tlv107(self):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00 00")
        pk.SetHex("00")
        pk.SetHex("00 00")
        pk.SetHex("01")
        return(self.tlv_pk("01 07", pk.GetAll()))
    def tlv108(self,_ksid):
        _ksid = []
        return(self.tlv_pk("01 08", _ksid))
    def tlv144(self,TGTKey,tlv109,tlv124,tlv128,tlv16e):
        # print TGTKey,tlv109,tlv124,tlv128,tlv16e
        pk = _pack()
        pk.Empty()
        pk.SetShort(4)
        pk.SetBin(tlv109)
        pk.SetBin(tlv124)
        pk.SetBin(tlv128)
        pk.SetBin(tlv16e)
        # print "pkall",pk.GetAll()
        return(self.tlv_pk("01 44", Hash.QQTEA(pk.GetAll(), TGTKey)))
    def tlv109(self,imei_):
        pk = _pack()
        return(self.tlv_pk("01 09", imei_))
    def tlv124(self,os_type,os_version,_network_type,_apn):
        pk = _pack()
        pk.SetShort(len(os_type))
        pk.SetStr(os_type)
        pk.SetShort(len(os_version))
        pk.SetStr(os_version)
        pk.SetShort(_network_type)
        pk.SetHex("00 00")
        pk.SetHex("00 00")
        pk.SetShort(len(_apn))
        pk.SetStr(_apn)
        return(self.tlv_pk("01 24", pk.GetAll()))
    def tlv128(self,_device,imei_):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00 00")
        pk.SetHex("00")
        pk.SetHex("01")
        pk.SetHex("01")
        pk.SetHex("01 00 02 00")
        pk.SetShort(len(_device))
        pk.SetStr(_device)
        pk.SetShort(len(imei_))
        pk.SetBin(imei_)
        pk.SetHex("00 00")
        return(self.tlv_pk("01 28", pk.GetAll()))
    def tlv16e(self,_device):
        pk = _pack()
        pk.Empty()
        pk.SetBin(tozjj(_device,"str",0))
        return(self.tlv_pk("01 6E", pk.GetAll()))
    def tlv142(self,_apk_id):
        pk = _pack()
        pk.Empty()
        pk.SetInt(len(tozjj(_apk_id,"str")))
        pk.SetBin(tozjj(_apk_id,"str"))
        return(self.tlv_pk("01 42", pk.GetAll()))
    def tlv154(self,_sso_seq):
        pk = _pack()
        pk.Empty()
        pk.SetInt(_sso_seq)
        return(self.tlv_pk("01 54", pk.GetAll()))
    def tlv145(self,imei_):
        pk = _pack()
        pk.Empty()
        pk.SetBin(imei_)
        return(self.tlv_pk("01 45", pk.GetAll()))
    def tlv141(self,_network_type,_apn):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00 01")
        pk.SetHex("00 00")
        pk.SetShort(_network_type)
        pk.SetShort(len(_apn))
        pk.SetStr(_apn)
        return(self.tlv_pk("01 41", pk.GetAll()))
    def tlv8(self):
        pk = _pack()
        pk.SetHex("00 00 ")
        pk.SetHex("00 00 08 04")
        pk.SetHex("00 00")
        return(self.tlv_pk("00 08", pk.GetAll()))
    def tlv16b(self):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00 01")
        pk.SetHex(" 00 0B")
        pk.SetHex("67 61 6D 65 2E 71 71 2E 63 6F 6D")
        return(self.tlv_pk("01 6B", pk.GetAll()))
    def tlv147(self,_apk_v,_apk_sig):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00 00 00 10")
        pk.SetShort(len(_apk_v))
        pk.SetStr(_apk_v)
        pk.SetShort(len(_apk_sig))
        pk.SetBin(_apk_sig)
        return(self.tlv_pk("01 47", pk.GetAll()))
    def tlv177(self):
        pk = _pack()
        pk.Empty()
        pk.SetHex("01")
        pk.SetHex("53 FB 17 9B")
        pk.SetHex("00 07")
        pk.SetHex("35 2E 32 2E 33 2E 30")
        return(self.tlv_pk("01 77", pk.GetAll()))
    def tlv114_get0058(self,b):
        unPack = _unpack()
        unPack.SetData(b)
        unPack.GetBin(6)
        l = unPack.GetShort()
        if(l != 88):
            print "error tlv114_get0058 l != 0058"
        return(unPack.GetBin(l))
    def tlv187(self):
        pk = _pack()
        pk = _pack()
        pk.Empty()
        pk.SetHex("F8 FF 12 23 6E 0D AF 24 97 CE 7E D6 A0 7B DD 68")
        return(self.tlv_pk("01 87", pk.GetAll()))
    def tlv188(self):
        pk = _pack()
        pk.Empty()
        pk.SetHex("4D BF 65 33 D9 08 C2 73 63 6D E5 CD AE 83 C0 43")
        return(self.tlv_pk("01 88", pk.GetAll()))
    def tlv191(self):
        pk = _pack()
        pk.Empty()
        pk.SetHex("00")
        return(self.tlv_pk("01 91", pk.GetAll()))

class JceInputStream:
    def __init__(self):
        self.unpackReq = _unpack()
        # 常量：
        self.login_state_logining = 0  # 正在登陆
        self.login_state_veriy = 1  # 需要验证码
        self.login_state_success = 2  # 验证成功
        self.TYPE_BYTE = 0 
        self.TYPE_DOUBLE = 5 
        self.TYPE_FLOAT = 4 
        self.TYPE_INT = 2 
        self.TYPE_JCE_MAX_STRING_LENGTH = 104857600 
        self.TYPE_LIST = 9 
        self.TYPE_LONG = 3 
        self.TYPE_MAP = 8 
        self.TYPE_SHORT = 1 
        self.TYPE_SIMPLE_LIST = 13 
        self.TYPE_STRING1 = 6 
        self.TYPE_STRING4 = 7 
        self.TYPE_STRUCT_BEGIN = 10 
        self.TYPE_STRUCT_END = 11 
        self.TYPE_ZERO_TAG = 12 
        self.Event_Get_Firends = 1  # 自己的好友
        self.Event_Get_Neighbor = 2  # 附近人
    def wrap(self,b):
        self.unpackReq.SetData(b)
    def SkipToTag(self,p_tag):  # 跳到指定tag处
        localHeadData = dt.HeadData();step = 0;
        while 1:
            step = self.peakHead(localHeadData)
            if(localHeadData.typ  == self.TYPE_STRUCT_END):
                break
            if(localHeadData.tag <= p_tag):
                if(localHeadData.tag != p_tag):
                    break
                return 1
            else:
                return 0
            self.skip(step)
            self.skipField(localHeadData.typ)
        return 0
    def skipField(self,p_type):
        t_len = 0;localHeadData = dt.HeadData();
        t_count = 0;i = 0;
        if(p_type  ==  self.TYPE_BYTE):
            self.skip(1)
        elif(p_type  ==  self.TYPE_SHORT):
            self.skip(2)
        elif(p_type  ==  self.TYPE_INT):
            self.skip(4)
        elif(p_type  ==  self.TYPE_LONG):
            self.skip(8)
        elif(p_type  ==  self.TYPE_SIMPLE_LIST):
            self.unpackReq.GetByte()
            localHeadData = self.ReadHead(localHeadData)[0]
            if(localHeadData.typ == self.TYPE_ZERO_TAG):
                pass
            else:
                if(localHeadData.typ  ==  self.TYPE_SHORT):
                    t_len = self.unpackReq.GetShort()
                else:
                    t_len = self.unpackReq.GetByte()
                self.skip(t_len)
        elif(p_type  ==  self.TYPE_MAP):
            localHeadData = self.ReadHead(localHeadData)[0]
            if(localHeadData.typ  ==  self.TYPE_ZERO_TAG):
                pass
            else:
                localHeadData = self.ReadHead(localHeadData)[0]
                t_count = localHeadData.typ
                for i in range(t_count):
                    localHeadData = self.ReadHead(localHeadData)[0]
                    self.skipField(localHeadData.typ)
                    localHeadData = self.ReadHead(localHeadData)[0]
                    self.skipField(localHeadData.typ)
        elif(p_type  ==  self.TYPE_ZERO_TAG):
            pass
        elif(p_type  ==  self.TYPE_STRING1):
            t_len = self.unpackReq.GetByte()
            self.skip(t_len)
        elif(p_type  ==  self.TYPE_LIST):
            localHeadData = self.ReadHead(localHeadData)[0]
            if(localHeadData.typ  ==  self.TYPE_ZERO_TAG):
                pass
            else:
                if(localHeadData.typ  ==  self.TYPE_SHORT):
                    t_count = self.unpackReq.GetShort()
                else:
                    t_count = self.unpackReq.GetByte()
                for i in range(t_count):
                    localHeadData = self.ReadHead(localHeadData)[0]
                    self.skipField(localHeadData.typ)
        elif(p_type  ==  self.TYPE_STRING4):
            t_len = self.unpackReq.GetInt()
            self.skip(t_len)
        elif(p_type  ==  self.TYPE_STRUCT_BEGIN):
            localHeadData = self.ReadHead(localHeadData)[0]
            while(localHeadData.typ != self.TYPE_STRUCT_END):
                self.skipField(localHeadData.typ)
                localHeadData = self.ReadHead(localHeadData)[0]
        else:
            print "error skipField  typ = ",p_type
    def skip(self,step):
        self.unpackReq.GetBin(step)
    def peakHead(self,localHeadData):
        return self.ReadHead(localHeadData,self.unpackReq.GetAll())[1]
    def ReadHead(self,paramHead,buffer = []):
        i = 0;unptmp = _unpack();ptmp = _pack();
        if(buffer == []):
            i = self.unpackReq.GetByte()
            paramHead.typ = i&15
            paramHead.tag  = (i&240)>>4
            if(paramHead.tag  ==  15):
                paramHead.tag = self.unpackReq.GetByte()
                return paramHead,2
            return paramHead,1
        else:
            ptmp.Empty()
            ptmp.SetBin(buffer)
            unptmp.SetData(ptmp.GetAll())
            i = unptmp.GetByte()
            paramHead.typ = i&15
            paramHead.tag  = (i&240)>>4
            if(paramHead.tag  ==  15):
                paramHead.tag = unptmp.GetByte()
                return paramHead,2
            return paramHead,1
    def ReadObj(self,typ):
        t_val = "";t_len = 0;localHeadData = dt.HeadData;t_count = 0;i = 0;
        if(typ == self.TYPE_BYTE):
            t_val  = str(self.unpackReq.GetByte())
        elif(typ == self.TYPE_SHORT):
            t_val  = str(self.unpackReq.GetShort())
        elif(typ == self.TYPE_INT):
            t_val  = str(self.unpackReq.GetInt())
        elif(typ == self.TYPE_LONG):
            t_val  = str(self.unpackReq.GetLong())
        elif(typ == self.TYPE_SIMPLE_LIST):
            self.unpackReq.GetByte()
            if(self.unpackReq.GetByte() == self.TYPE_SHORT):
                t_len = self.unpackReq.GetShort()
            else:
                t_len = self.unpackReq.GetByte()
            t_val = tohex(self.unpackReq.GetBin(t_len))
        elif(typ == self.TYPE_MAP):
            localHeadData = self.ReadHead(localHeadData)[0]
            t_val = "{"
            if(typ == self.TYPE_ZERO_TAG):
                pass
            else:
                localHeadData = self.ReadHead(localHeadData)[0]
                t_count = typ
                for i in range(t_count):
                    localHeadData = self.ReadHead(localHeadData)[0]
                    t_val = t_val + "k = " + self.ReadObj(localHeadData.typ)
                    localHeadData = self.ReadHead(localHeadData)[0]
                    t_val = t_val + ",  v = " + self.ReadObj(localHeadData.typ) + "  "
            t_val = t_val + "}"
        elif(typ == self.TYPE_ZERO_TAG):
            t_val = "0"
        elif(typ == self.TYPE_STRING1):
            t_len = self.unpackReq.GetByte()
            t_val = list2str(self.unpackReq.GetBin(t_len)+[0])
        elif(typ == self.TYPE_LIST):
            localHeadData = self.ReadHead(localHeadData)[0]
            t_val = "["
            if(typ == self.TYPE_ZERO_TAG):
                pass
            else:
                if(typ == self.TYPE_SHORT):
                    t_count = self.unpackReq.GetShort()
                else:
                    t_count = self.unpackReq.GetByte()
                for i in range(t_count):
                    localHeadData = self.ReadHead(localHeadData)[0]
                    t_val = t_val + "" + self.ReadObj(localHeadData.typ)
                    if(i != t_count):
                        t_val = t_val + ","
            t_val = t_val + "]"
        elif(typ == self.TYPE_STRING4):
            t_len = self.unpackReq.GetInt()
            t_val = list2str(self.unpackReq.GetBin(t_len)+[0])
        elif(typ == self.TYPE_STRUCT_BEGIN):
            localHeadData = self.ReadHead(localHeadData)[0]
            if(localHeadData.typ != self.TYPE_STRUCT_END):
                t_val = t_val + self.ReadObj(localHeadData.typ)
                localHeadData = self.ReadHead(localHeadData)[0]
        else:
            print "error ReadValNum  typ = " ,typ
        return t_val
    def ReadByte(self,p_tag):
        localHeadData = dt.HeadData();paramByte = 0;
        if(self.SkipToTag(p_tag) == 0):
            return(paramByte)
        localHeadData = self.ReadHead(localHeadData)[0]
        if(localHeadData.typ == self.TYPE_ZERO_TAG):
            paramByte = 0
        elif(localHeadData.typ == self.TYPE_BYTE):
            paramByte = self.unpackReq.GetByte()
        elif(localHeadData.typ == self.TYPE_SHORT):
            paramByte = self.unpackReq.GetShort()
        else:
            print "read Byte :error typ mismatch"
        return(paramByte)
    def ReadShort(self,p_tag):
        localHeadData = dt.HeadData();paramByte = 0;
        if(self.SkipToTag(p_tag) == 0):
            return(paramByte)
        localHeadData = self.ReadHead(localHeadData)[0]
        if(localHeadData.typ == self.TYPE_ZERO_TAG):
            paramByte = 0
        elif(localHeadData.typ == self.TYPE_BYTE):
            paramByte = self.unpackReq.GetByte()
        elif(localHeadData.typ == self.TYPE_SHORT):
            paramByte = self.unpackReq.GetShort()
        else:
            print "read short :error typ mismatch"
        return(paramByte)
    def ReadInt(self,p_tag):
        localHeadData = dt.HeadData();paramByte = 0;
        if(self.SkipToTag(p_tag) == 0):
            return(paramByte)
        localHeadData = self.ReadHead(localHeadData)[0]
        if(localHeadData.typ == self.TYPE_ZERO_TAG):
            paramByte = 0
        elif(localHeadData.typ == self.TYPE_BYTE):
            paramByte = self.unpackReq.GetByte()
        elif(localHeadData.typ == self.TYPE_SHORT):
            paramByte = self.unpackReq.GetShort()
        elif(localHeadData.typ == self.TYPE_INT):
            paramByte = self.unpackReq.GetInt()
        else:
            print "read int :error typ mismatch"
        return(paramByte)
    def ReadLong(self,p_tag):
        localHeadData = dt.HeadData();paramByte = 0;
        if(self.SkipToTag(p_tag) == 0):
            return(paramByte)
        localHeadData = self.ReadHead(localHeadData)[0]
        if(localHeadData.typ == self.TYPE_ZERO_TAG):
            paramByte = 0
        elif(localHeadData.typ == self.TYPE_BYTE):
            paramByte = self.unpackReq.GetByte()
        elif(localHeadData.typ == self.TYPE_SHORT):
            paramByte = self.unpackReq.GetShort()
        elif(localHeadData.typ == self.TYPE_INT):
            paramByte = self.unpackReq.GetInt()
        elif(localHeadData.typ == self.TYPE_LONG):
            paramByte = self.unpackReq.GetLong()
        else:
            print "read int :error typ mismatch"
        return(paramByte)
    def ReadString(self,p_tag):
        localHeadData = dt.HeadData();t_val = "";t_len = 0;
        if(self.SkipToTag(p_tag) == 0):
            return(t_val)
        localHeadData = self.ReadHead(localHeadData)[0]
        if(localHeadData.typ == self.TYPE_ZERO_TAG):
            pass
        elif(localHeadData.typ == self.TYPE_STRING1):
            t_len = self.unpackReq.GetByte()
            t_val = list2str(self.unpackReq.GetBin(t_len))
        elif(localHeadData.typ == self.TYPE_STRING4):
            t_len = self.unpackReq.GetInt()
            t_val = list2str(self.unpackReq.GetBin(t_len))
        return(t_val)
    def ReadSimpleList(self,p_tag):
        localHeadData = dt.HeadData()
        t_val = []
        t_l = 0
        t_type = 0
        if(self.SkipToTag(p_tag) == 0):
            return(t_val)
        localHeadData = self.ReadHead(localHeadData)[0]
        if(localHeadData.typ == self.TYPE_SIMPLE_LIST):
            self.unpackReq.GetByte()
            t_type = self.unpackReq.GetByte()
            if(t_type == self.TYPE_ZERO_TAG):
                return(t_val)
            else:
                if(t_type == self.TYPE_SHORT):
                    t_l = self.unpackReq.GetShort()
                else:
                    t_l = self.unpackReq.GetByte()
            t_val = self.unpackReq.GetBin(t_l)
        return(t_val)
    def ReadList(self,p_tag,ret_arr = []):
        localHeadData = dt.HeadData()
        t_val = ""
        t_count = 0
        i = 0
        if(self.SkipToTag(p_tag) == 0):
            return(t_val)
        localHeadData = self.ReadHead(localHeadData)[0]
        if(localHeadData.typ == self.TYPE_ZERO_TAG):
            pass
        elif(localHeadData.typ == self.TYPE_LIST):
            t_count = self.ReadShort(0)
            for i in range(t_count):
                localHeadData = self.ReadHead(localHeadData)[0]
                t_val = self.ReadObj(localHeadData.typ)
                ret_arr.append(t_val)
    def ReadType(self):
        localHeadData = dt.HeadData()
        localHeadData = self.ReadHead(localHeadData)[0]
        return localHeadData.typ
    def ReadToTag(self,p_tag):     # 返回type -1没找到
        localHeadData = dt.HeadData()
        if(self.SkipToTag(p_tag) == 0):
            return -1
        localHeadData = self.ReadHead(localHeadData)[0]
        return localHeadData.typ
    def skipToEnd(self):
        te = "";localHeadData = dt.HeadData();step = 0;
        for i in range(100):
            te = tohex(self.unpackReq.GetAll())
            localHeadData,step = self.ReadHead(localHeadData)
            te = tohex(self.unpackReq.GetAll())
            if(localHeadData.typ == self.TYPE_ZERO_TAG):
                continue
            if(localHeadData.typ == self.TYPE_STRUCT_END):
                break
            self.skipField(localHeadData.typ)
    def ReadMap(self,p_tag,p_val):
        localHeadData = dt.HeadData()
        t_val = ""
        t_count = 0
        i = 0
        t_map = dt.JceMap()
        if(self.SkipToTag(p_tag) == 0):
            return
        localHeadData = self.ReadHead(localHeadData)[0]
        if(localHeadData.typ != self.TYPE_MAP):
            return
        localHeadData = self.ReadHead(localHeadData)[0]
        if(localHeadData.typ == self.TYPE_ZERO_TAG):
            pass
        else:
            if(localHeadData.typ == self.TYPE_SHORT):
                t_count = self.unpackReq.GetShort()
            else:
                t_count = self.unpackReq.GetByte()
            for i in range(t_count):
                localHeadData = self.ReadHead(localHeadData)[0]
                t_val = self.ReadObj(localHeadData.typ)
                t_map.key_type = localHeadData.typ
                t_map.key = tozjj(t_val,"str",0)
                localHeadData = self.ReadHead(localHeadData)[0]
                t_val = self.ReadObj(localHeadData.typ)
                t_map.val_type = localHeadData.typ
                t_map.val  = tozjj(t_val,"str",0)
                p_val.append(t_map)
    def getAll(self):
        return self.unpackReq.GetAll()
class JceOutputStream:
    def __init__(self):
        self.pk = _pack()
        # 常量：
        self.login_state_logining = 0  # 正在登陆
        self.login_state_veriy = 1  # 需要验证码
        self.login_state_success = 2  # 验证成功
        self.TYPE_BYTE = 0 
        self.TYPE_DOUBLE = 5 
        self.TYPE_FLOAT = 4 
        self.TYPE_INT = 2 
        self.TYPE_JCE_MAX_STRING_LENGTH = 104857600 
        self.TYPE_LIST = 9 
        self.TYPE_LONG = 3 
        self.TYPE_MAP = 8 
        self.TYPE_SHORT = 1 
        self.TYPE_SIMPLE_LIST = 13 
        self.TYPE_STRING1 = 6 
        self.TYPE_STRING4 = 7 
        self.TYPE_STRUCT_BEGIN = 10 
        self.TYPE_STRUCT_END = 11 
        self.TYPE_ZERO_TAG = 12 
        self.Event_Get_Firends = 1  # 自己的好友
        self.Event_Get_Neighbor = 2  # 附近人
    def clear(self):
        self.pk.Empty()
    def toByteArray(self):
        return self.pk.GetAll()
    def wrap(self,b):
        self.pk.SetData(b)
    def WriteHead(self,p_val,p_tag):
        t_val = 0
        if(p_tag >= 15):
            t_val = p_val|240
            self.pk.SetByte(t_val)
            self.pk.SetByte(p_tag)
        else:
            t_val = p_val|(p_tag<<4)
            self.pk.SetByte(t_val)
    def WriteObj(self,p_type,p_val,p_tag):
        if(p_type == self.TYPE_BYTE):
            self.WriteByte(int(p_val), p_tag)
        elif(p_type == self.TYPE_SHORT):
            self.WriteShort(int(p_val), p_tag)
        elif(p_type == self.TYPE_INT):
            self.WriteInt(int(p_val), p_tag)
        elif(p_type == self.TYPE_LONG):
            self.WriteLong(long(p_val), p_tag)
        elif(p_type == self.TYPE_SIMPLE_LIST):
            self.WriteSimpleList(p_val, p_tag)
        elif(p_type == self.TYPE_MAP):
            print "error can# t write map "
        elif(p_type == self.TYPE_STRING1):
           self.WriteStringByte(list2str(p_val), p_tag)
        elif(p_type == self.TYPE_LIST):
            self.WriteList(p_val, p_tag)
        elif(p_type == self.TYPE_STRING4):
           self.WriteStringByte(list2str(p_val), p_tag)
        else:
            print "error self.WriteObj  typ = "+p_type
    def WriteByte(self,p_val,p_tag):
        if(p_val == 0):
            self.WriteHead(self.TYPE_ZERO_TAG, p_tag)
        else:
            self.WriteHead(self.TYPE_BYTE, p_tag)
            self.pk.SetByte(p_val)
    def WriteShort(self,p_val,p_tag):
        if(p_val >= -128 and p_val <= 127):
            self.WriteByte(p_val, p_tag)
        else:
            self.WriteHead(self.TYPE_SHORT, p_tag)
            self.pk.SetShort(p_val)
    def WriteInt(self,p_val,p_tag):
        if(p_val >= -32768 and p_val <= 32767):
            self.WriteShort(p_val, p_tag)
        else:
            self.WriteHead(self.TYPE_INT, p_tag)
            self.pk.SetInt(p_val)
    def WriteLong(self,p_val,p_tag):
        #print "p_val",p_val
        if(p_val >= -2147483648 and p_val <= 2147483647):
            self.WriteInt(int(p_val), p_tag)
        else:
            self.WriteHead(self.TYPE_LONG, p_tag)
            self.pk.SetBin(Xbin.Long2Bin(p_val))
    def WriteByteString(self,p_val,p_tag):    # 十六进制字节
        t_val = []
        t_val = tozjj(p_val,"str2")
        if(len(t_val) > 255):
            self.WriteHead(self.TYPE_STRING4, p_tag)
            self.pk.SetInt(len(t_val))
            self.pk.SetBin(t_val)
        else:
            self.WriteHead(self.TYPE_STRING1, p_tag)
            self.pk.SetByte(len(t_val))
            self.pk.SetBin(t_val)
    def WriteStringByte(self,p_val,p_tag):
        t_val = []
        t_val = tozjj(p_val,"str",0)
        # print "p_val tval",p_val,t_val
        #t_val = t_val
        # print "tval2",t_val
        if(len(t_val)>255):
            self.WriteHead(self.TYPE_STRING4, p_tag)
            self.pk.SetInt(len(t_val))
            self.pk.SetBin(t_val)
        else:
            self.WriteHead(self.TYPE_STRING1, p_tag)
            self.pk.SetByte(len(t_val))
            self.pk.SetBin(t_val)
    def WriteJceStruct(self,p_val,p_tag):
        self.WriteHead(self.TYPE_STRUCT_BEGIN, p_tag)
        #print "pval",len(p_val),p_val
        self.pk.SetBin(p_val)
        self.WriteHead(self.TYPE_STRUCT_END,0)
    def WriteSimpleList(self,p_val,p_tag):
        self.WriteHead(self.TYPE_SIMPLE_LIST, p_tag)
        self.WriteHead(0,0)
        #print "len",len(p_val),p_val
        self.WriteInt(len(p_val),0)
        self.pk.SetBin(p_val)
    def WriteList(self,p_val,p_tag):
        self.WriteHead(self.TYPE_LIST, p_tag)
        self.WriteInt(len(p_val),0)
        for i in range(len(p_val)):
            self.WriteInt(p_val[i],0)
    def WriteMap(self,p_key,p_tag):
        i = 0;l = 0;
        #print "p_key123",len(p_key),p_key[0].key,p_tag
        # print "s-1",self.toByteArray()
        self.WriteHead(self.TYPE_MAP, p_tag)
        # print "s0",self.toByteArray()
        l = len(p_key)
        #print "map1",l
        self.WriteShort(l, 0)
        # print "s1",self.toByteArray()
        if(l == 0):return
        for i in range(l):
            #print "i ",i
            self.WriteObj(p_key[i].key_type,p_key[i].key,0)
            #print "s2",len(self.toByteArray()),self.toByteArray()
            self.WriteObj(p_key[i].val_type,p_key[i].val,1)
            #print "s3",len(self.toByteArray()),self.toByteArray()
    def putHex(self,h):
        self.pk.SetHex(h)
class JceFormat:
    def __init__(self):
        self.typ = 0
        self.tag = 0
        self.unpackReq = _unpack()
        # 常量：
        self.login_state_logining = 0  # 正在登陆
        self.login_state_veriy = 1  # 需要验证码
        self.login_state_success = 2  # 验证成功
        self.TYPE_BYTE = 0 
        self.TYPE_DOUBLE = 5 
        self.TYPE_FLOAT = 4 
        self.TYPE_INT = 2 
        self.TYPE_JCE_MAX_STRING_LENGTH = 104857600 
        self.TYPE_LIST = 9 
        self.TYPE_LONG = 3 
        self.TYPE_MAP = 8 
        self.TYPE_SHORT = 1 
        self.TYPE_SIMPLE_LIST = 13 
        self.TYPE_STRING1 = 6 
        self.TYPE_STRING4 = 7 
        self.TYPE_STRUCT_BEGIN = 10 
        self.TYPE_STRUCT_END = 11 
        self.TYPE_ZERO_TAG = 12 
        self.Event_Get_Firends = 1  # 自己的好友
        self.Event_Get_Neighbor = 2  # 附近人
    def wrap(self,b):
        self.unpackReq.SetData(b)
    def ReadValNum(self,space):
        t_val = "";t_len = 0;localHeadData = dt.HeadData();t_count = 0;
        if(self.typ == self.TYPE_BYTE):
            t_val = str(self.unpackReq.GetByte())
        elif(self.typ == self.TYPE_SHORT):
            t_val = str(self.unpackReq.GetShort())
        elif(self.typ == self.TYPE_INT):
            t_val = str(self.unpackReq.GetInt())
        elif(self.typ == self.TYPE_LONG):
            t_val = str(self.unpackReq.GetLong())
        elif(self.typ == self.TYPE_SIMPLE_LIST):
            self.unpackReq.GetByte()
            if(self.unpackReq.GetByte() == self.TYPE_SHORT):
                t_l = self.unpackReq.GetShort()
            else:
                t_l = self.unpackReq.GetByte()
            t_val = tozjj(self.unpackReq.GetBin(t_l))
        elif(self.typ == self.TYPE_MAP):
            localHeadData = self.ReadHead(localHeadData)[0]
            t_val = "{"
            if(self.typ == self.TYPE_ZERO_TAG):
                pass
            else:
                localHeadData = self.ReadHead(localHeadData)[0]
                t_count = self.typ
                t_val = t_val + "\n"
                for i in range(t_count):
                    localHeadData = self.ReadHead(localHeadData)[0]
                    t_val = t_val + "k = " + self.ReadValNum(space)
                    localHeadData = self.ReadHead(localHeadData)[0]
                    t_val = t_val + ",  v = " + self.ReadValNum(space)+"  "
                    if(i != t_count):
                        t_val = t_val + "\n"
            t_val = t_val + "}"
        elif(self.typ == self.TYPE_ZERO_TAG):
            t_val = "0"
        elif(self.typ == self.TYPE_STRING1):
            t_l = self.unpackReq.GetByte()
            t_val = list2str(self.unpackReq.GetBin(t_l))
        elif(self.typ == self.TYPE_LIST):
            localHeadData = self.ReadHead(localHeadData)[0]
            t_val = "["
            if(self.typ == self.TYPE_ZERO_TAG):
                pass
            else:
                t_val = t_val + "\n"
                for i in range(t_count):
                    while(i>0):
                        localHeadData = self.ReadHead(localHeadData)[0]
                        if(localHeadData.typ == self.TYPE_STRUCT_END):
                            break
                        if(localHeadData.typ == self.TYPE_STRUCT_BEGIN):
                            continue
                        t_val = t_val + " "*(space + 1) + "[" + str(localHeadData.tag) + " " + str(localHeadData.typ) + " " + "]" + self.ReadValNum(space) + "\n"
                    if(i != t_count):
                        t_val = t_val + "\n"
                if(t_count == 0):
                    t_val = t_val+"\n"
            t_val = t_val + "]"
        elif(self.typ == self.TYPE_STRING4):
            t_l = self.unpackReq.GetInt()
            t_val = list2str(self.unpackReq.GetBin(t_l))
        else:
            print "error ReadValNum  typ = ",str(self.typ)
        return(t_val)
    def ReadHead(self,paramHead,buffer = []):
        i = 0;unptmp = _unpack();ptmp = _pack();
        if(buffer == []):
             i = self.unpackReq.GetByte()
        else:
            ptmp.Empty()
            ptmp.SetBin(buffer)
            unptmp.SetData(ptmp.GetAll())
            i = unptmp.GetByte()
        self.typ = i&15
        self.tag = (i&240)>>4
        paramHead.typ = self.typ
        paramHead.tag = self.tag
        if(paramHead.tag  ==  15):
            paramHead.tag = self.unpackReq.GetByte()
            return paramHead,2
        return paramHead,1
    def getName(self,nameArr,p_tag):
        t_len = 0
        t_len = len(nameArr)
        if(t_len>0 and p_tag <= t_len):
            return nameArr[p_tag+1]
        return ""
    def format_requestPack(self):
        t_name_arr = ["" for i in range(10)]
        localHeadData = dt.HeadData();
        t_text = "";t_name = "";
        t_name_arr = ["", "iversion", "cPacketType", "iMessageType", "iRequestId", "sServantName", "sFuncName", "sBuffer", "iTimeout", "context", "status"]
        while 1:
            localHeadData = self.ReadHead(localHeadData)[0]
            t_name = self.getName(t_name_arr, self.tag)
            t_text = t_text + "[" + localHeadData.tag + " " + localHeadData.typ + " " + t_name + "]" + self.ReadValNum(0) + "\n"
            if(len(self.unpackReq.GetAll()) != 0):break
        return t_text
    def format_JceStruct(self):
        localHeadData = dt.HeadData();t_text = ""
        while 1:
            localHeadData = self.ReadHead(localHeadData)[0]
            if(self.typ != self.TYPE_STRUCT_BEGIN and self.typ != self.TYPE_STRUCT_END):
                t_text = t_text+"[" + localHeadData.tag + " " + localHeadData.typ + " " + "]" + self.ReadValNum(0) + "\n"
            if(len(self.unpackReq.GetAll())  !=  0):break
        return(t_text)
    def format_pack_top(self):
        ssoSeq_ = 0;appId = 0;serviceCmd = "";msgCookies = [];t_text = "";t_len = 0;
        ssoSeq_ = self.unpackReq.GetInt()
        t_text = t_text + "ssoSeq_ = " + str(ssoSeq_) + "\n"
        appId = self.unpackReq.GetInt()
        t_text = t_text + "appId = " + str(appId) + "\n"
        appId = self.unpackReq.GetInt()
        t_text = t_text + "appId = " + str(appId) + "\n"
        t_text = t_text + "00 = " + str(tohex(self.unpackReq.GetBin(12))) + "\n"
        t_l = self.unpackReq.GetInt() - 4
        t_text = t_text + "extBin = " + str(tohex(self.unpackReq.GetBin(t_l))) + "\n"
        t_l = self.unpackReq.GetInt() - 4
        serviceCmd = list2str(self.unpackReq.GetBin(t_l) + { 0 })
        t_text = t_text + "serviceCmd = " + serviceCmd + "\n"
        t_l = self.unpackReq.GetInt() - 4
        t_text = t_text + "msgCookies = " + str(tohex(self.unpackReq.GetBin(t_l))) + "\n"
        t_l = self.unpackReq.GetInt() - 4
        t_text = t_text + "imei = " + str(tohex(self.unpackReq.GetBin(t_l))) + "\n"
        t_l = self.unpackReq.GetInt() - 4
        t_text = t_text + "ksid = " + str(tohex(self.unpackReq.GetBin(t_l))) + "\n"
        t_l = self.unpackReq.GetShort() - 2
        t_text = t_text + "ver = " + str(tohex(self.unpackReq.GetBin(t_l))) + "\n"
        return(t_text)
class JceStruct_Display:
    def __init__(self):
        pass
    def Display_RequestPacket(self,struct_):
        i = 0;displayer = "";space = 0;
        displayer = displayer +" "*space+ "iversion = " +str(struct_.iversion) +"\n"
        displayer = displayer +" "*space+ "cPacketType = " +str(struct_.cPacketType) +"\n"
        displayer = displayer +" "*space+ "iMessageType = " +str(struct_.iMessageType) +"\n"
        displayer = displayer +" "*space+ "iRequestId = " +str(struct_.iRequestId) +"\n"
        displayer = displayer +" "*space+ "sServantName = " +str(struct_.sServantName) +"\n"
        displayer = displayer +" "*space+ "sFuncName = " +str(struct_.sFuncName) +"\n"
        displayer = displayer +" "*space+ "sBuffer = " + tozjj(struct_.sBuffer) +"\n"
        displayer = displayer +" "*space+ "iTimeout = " +str(struct_.iTimeout) +"\n"
        displayer = displayer +" "*space+ "context = {"
        for i in range(len(struct_.context)):
            displayer = displayer +" "*(space + 2) +str(struct_.context [i].key) + ":" + tozjj(struct_.context [i].val) +"\n"
        displayer = displayer +" "*space+ "}" +"\n"
        displayer = displayer +" "*space+ "status = {"
        for i in range(len(struct_.status)):
            displayer = displayer +" "*(space + 2) +str(struct_.status [i].key) + ":" + tozjj(struct_.status [i].val) +"\n"
        displayer = displayer +" "*space+ "}" +"\n"
        return(displayer)
if __name__  ==  "__main__":
    a = Android()
    #b = [ 2, 2, 140, 31, 65, 8, 16, 0, 1, 7, 91, 205, 21, 3, 7, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 179, 166, 219, 60, 135, 12, 62, 153, 36, 94, 13, 28, 6, 183, 71, 222, 1, 2, 0, 25, 2, 36, 75, 121, 242, 35, 151, 85, 231, 60, 115, 255, 88, 61, 78, 197, 98, 92, 25, 191, 128, 149, 68, 109, 225, 145, 226, 48, 146, 52, 193, 117, 28, 95, 84, 142, 189, 124, 211, 112, 11, 178, 220, 151, 159, 12, 102, 102, 163, 228, 240, 254, 80, 56, 49, 72, 46, 144, 56, 27, 124, 20, 32, 194, 104, 111, 255, 54, 116, 113, 143, 187, 154, 166, 174, 194, 237, 151, 2, 126, 116, 0, 153, 104, 5, 97, 11, 142, 2, 76, 50, 210, 116, 145, 107, 244, 133, 127, 23, 140, 213, 237, 177, 252, 156, 24, 165, 109, 231, 220, 208, 219, 46, 35, 81, 170, 61, 204, 190, 175, 49, 208, 93, 53, 234, 91, 48, 101, 79, 3, 117, 189, 253, 79, 123, 226, 251, 223, 202, 192, 44, 47, 151, 237, 240, 65, 31, 221, 69, 220, 122, 249, 148, 59, 168, 247, 156, 221, 135, 30, 190, 178, 51, 123, 196, 35, 168, 249, 89, 24, 103, 114, 142, 229, 77, 39, 173, 109, 35, 226, 77, 231, 104, 194, 43, 108, 88, 155, 158, 31, 27, 249, 204, 55, 200, 235, 165, 15, 77, 105, 101, 157, 124, 249, 127, 160, 15, 168, 80, 203, 169, 122, 175, 37, 2, 142, 168, 32, 3, 106, 102, 130, 222, 161, 124, 249, 188, 118, 205, 252, 144, 170, 229, 14, 150, 190, 126, 158, 70, 205, 121, 77, 183, 170, 203, 16, 125, 142, 55, 71, 78, 98, 140, 5, 209, 253, 193, 115, 139, 100, 254, 177, 18, 136, 84, 149, 209, 103, 165, 113, 79, 98, 39, 185, 203, 150, 78, 162, 217, 14, 45, 109, 208, 209, 85, 146, 9, 134, 138, 171, 248, 172, 131, 93, 150, 130, 169, 103, 137, 149, 177, 63, 158, 111, 15, 18, 150, 178, 98, 129, 3, 84, 238, 112, 231, 106, 242, 204, 18, 219, 73, 123, 68, 225, 234, 229, 150, 153, 82, 109, 142, 68, 87, 10, 59, 33, 58, 31, 87, 11, 87, 160, 179, 102, 107, 111, 99, 215, 208, 107, 244, 113, 241, 113, 43, 127, 42, 225, 92, 98, 160, 13, 34, 133, 72, 244, 233, 178, 166, 203, 151, 127, 154, 34, 124, 129, 89, 125, 58, 6, 153, 4, 170, 150, 204, 32, 237, 198, 166, 181, 230, 155, 40, 109, 17, 118, 156, 116, 210, 188, 175, 237, 134, 119, 116, 1, 50, 18, 55, 166, 75, 223, 160, 167, 191, 228, 210, 174, 135, 250, 54, 113, 104, 104, 62, 189, 82, 228, 150, 14, 45, 97, 37, 5, 184, 208, 15, 159, 237, 52, 141, 205, 241, 74, 218, 170, 213, 187, 161, 247, 17, 192, 152, 28, 152, 216, 32, 187, 197, 139, 40, 10, 187, 213, 137, 65, 62, 115, 43, 79, 220, 139, 160, 202, 207, 122, 132, 30, 194, 188, 130, 32, 36, 92, 152, 63, 64, 172, 199, 11, 164, 184, 56, 178, 58, 236, 121, 240, 149, 53, 41, 107, 157, 14, 205, 138, 128, 173, 181, 77, 253, 57, 209, 192, 55, 145, 133, 83, 226, 181, 93, 128, 212, 222, 219, 12, 35, 235, 139, 80, 61, 84, 75, 142, 82, 36, 238, 154, 20, 54, 175, 47, 84, 66, 229, 95, 150, 238, 40, 230, 33, 61, 174, 180, 240, 18, 130, 223, 110, 70, 109, 64, 206, 54, 32, 117, 168, 102, 246, 1, 54, 121, 239, 47, 240, 1, 143, 196, 159, 226, 33, 234, 200, 243, 47, 100, 42, 216, 0, 35, 128, 125, 224, 245, 255, 83, 21, 191, 50, 116, 186, 3]
    a.init("123456789","123456789")
    a.QQ_loadTokenData()
    #a.Pack_StatSvc_Register_online()
    a.Pack_MessageSvc_offlinemsg(1311817771 , "123456")
    # a.Fun_Login()
    # print a.Make_login_sendSsoMsg("wtlogin.login",b,[],"866819027236658",[],[53, 46, 56, 46, 48, 46, 49, 53, 55, 49, 53, 56],1)
    #print "vm",a.Pack_VieryImage("1234")


