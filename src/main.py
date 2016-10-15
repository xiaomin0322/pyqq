# -*- coding: utf8 -*-
# 作者：Light.紫.星
# QQ：1311817771
import AndroidQQ,threading,time
from AndroidQQ import Android

class Main:
    def __init__(self):
        pass
    def login(self,qqnum,qqpass):
        print 15*"-",("开始登陆QQ："),qqnum,15*"-"
        self.sdk = Android()
        self.state = 0
        self.code = ""
        self.sdk.init(qqnum,qqpass)
        #self.sdk.QQ_loadTokenData()
        #self.state = self.sdk.Fun_again_Login ()
        #print "self.state",self.state
        self.state = self.sdk.Fun_Login()
        self.do_login()
    def do_login(self):
        if(self.state == self.sdk.login_state_success):
            self.sdk.QQ_online( );   #上线
            print "登陆成功"
            self.sdk.QQ_sendfriendmsg(635674608,"1234test测试") #发好友消息
            self.sdk.QQ_sendgroupmsg(189884897," 测试  test  43 2 1 ") #发群消息
            #self.sdk.QQ_offline( ); #下线
            # sdk.qq_savetokendata()# 保存二次登陆数据
            # 启动线程 (&循环处理消息, , thread_hwnd)
            return
        elif(self.state == self.sdk.login_state_veriy):
            print "需要验证码"
            open("vpic.jpg","wb").write(self.sdk.getViery())
            code = raw_input("请输入验证码(vpic.jpg):")
            self.state = self.sdk.Fun_SendCode(code)
            # self.state = self.sdk.Fun_SendCode("abcd")
            print  "验证码返回",self.state
            self.do_login()
        else:
            print "登陆失败：",self.sdk.getLastError()
if __name__  ==  "__main__":
    qq = Main()
    qq.login("634545399","")
