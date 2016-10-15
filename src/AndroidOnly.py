# -*- coding: utf8 -*-
# 作者：Light.紫.星
# QQ：1311817771
# 翻译自 易语言 安卓QQ协议模块源码
import md5,random
def list2str(data):
    t = ""
    for i in data:
        # print i
        t2 = str(hex(i)).replace("0x","").replace("L","")
        if(len(t2) == 1):t2 = "0"+t2
        t+= t2
    # print t,t.decode("hex")
    return t.decode("hex")
# print list2str("123456")
def tohex(t):
    all = ""
    for i in t:
        t2 = hex(int(i)).replace("0x","")
        if(len(t2) == 1):t2 = "0"+t2
        all+= t2
    return all.upper()

def findlist(rq,tt):
    pos1 = -1
    pos_tmp = 0
    for i in range(len(rq)):
        flag = 0
        pos_tmp+= 1
        for j in range(len(tt)):
            if(int(rq[i]) == int(tt[j])):
                i+= 1
                flag+= 1
            else:
                break
        # print flag
        if(flag == len(tt)):
            pos1 = pos_tmp
            break
    # print pos1
    return pos1
def inflate_Decompress(b):#zlib解压
    return b
def binmid(rq,a,b):
    return rq[(a-1):][:b]

def tozjj(data,method = "str2",thkg = 1):# 到字节集
    if(method == "str2"):
        if(thkg == 1):
            data = data.replace(" ","")
        t = []
        for i in range(0,len(data),2):
            try:t.append(int(data[i]+data[i+1], 16))
            except:break
        return t
    elif(method == "str"):
        if(thkg == 1):
            data = data.replace(" ","")
        data = data.encode("hex")
        t = []
        for i in range(0,len(data),2):
            try:t.append(int(data[i]+data[i+1], 16))
            except:break
        return t
    elif(method == "byte"):
        return [int(data)%256]
    elif(method == "int"):
        n = data
        t = []
        if n == 0:t = [0]
        while(n>0):
            m = n%256
            # print "m = ",m
            if(m == 0):m = 256
            t.append(m)
            n = (n-m)/256
            # print "n = ",n
        if(len(t)%4 != 0):
            for i in range(4-len(t)%4):
                t.append(0)
        return t
    elif(method=="long"):
        n = data
        t = [ ]
        if n == 0: t = [ 0 ]
        while (n > 0):
            m = n % 256
            # print "m = ",m
            if (m == 0): m = 256
            t.append( m )
            n = (n - m) / 256
            # print "n = ",n
        if (len( t ) % 8 != 0):
            for i in range( 8 - len( t ) % 8 ):
                t.append( 0 )
        return t
    elif(method == "short"):
        n = data
        t = []
        if n == 0:t = [0]
        while(n>0):
            m = n%256
            if(m == 0):m = 256
            t.append(m)
            n = (n-m)/256
        if(len(t)%2 != 0):
            t.append(0)
        return [t[0],t[1]]
    else:
        pass
class _hash:
    def __init__(self):
        self.m_plain = [0 for i in range(8)]
        self.m_preplain = [0 for i in range(8)]
        self.m_out = []
        self.m_crypt = 0
        self.m_precrypt = 0
        self.m_pos = 0
        self.m_padding = 0
        self.m_key = [0 for i in range(16)]
        self.m_header = True
        self.m_contextstart = 0
    def getuint(self,_input,ioffset,intlen):
        ret = 0;
        if(intlen>4):
            lend = ioffset+4
        else:
            lend = ioffset+intlen
        for i in range(ioffset,lend):
            ret = ret<<8
            try:
                ret = ret | _input[i-1]
            except:
                pass
                #print "error:",ioffset,lend
        return ret
    def tobytes(self,a,b):
        by = []
        by.append((a>>24)&255)
        by.append((a>>16)&255)
        by.append((a>>8)&255)
        by.append(a&255)
        by.append((b>>24)&255)
        by.append((b>>16)&255)
        by.append((b>>8)&255)
        by.append(b&255)
        return by
        
    def encipher(self,bininput,k,is16rounds):
        crypted = []
        su = 0;rounds = 0;y = 0;z = 0;a = 0;b = 0;c = 0;d = 0;test = 0;
        y = self.getuint(bininput,1,4)
        z = self.getuint(bininput,5,4)
        a = self.getuint(self.m_key,1,4)
        b = self.getuint(self.m_key,5,4)
        c = self.getuint(self.m_key,9,4)
        d = self.getuint(self.m_key,13,4)
        if(is16rounds):
            rounds = 16
        else:
            rounds = 32
        for i in range(rounds):
            su = su&4294967295
            su = su+2654435769
            z = z&4294967295
            y = y+((((z<<4)+a)^(z+su))^((z>>5)+b))
            y = y&4294967295
            z = z+((((y<<4)+c)^(y+su))^((y>>5)+d))
            # 加法优先级高于xor运算
        return self.tobytes(y,z)
    def Encrypt8Bytes(self,is16rounds):
        self.m_pos = 0;crypted = []
        for i in range(8):
            if(self.m_header):
                self.m_plain[i] = self.m_plain[i]^self.m_preplain[1]
            else:
                if(self.m_precrypt+i>len(self.m_out)):
                    return
                self.m_plain[i] = self.m_plain[i]^self.m_out[self.m_precrypt+i]
        crypted = self.encipher(self.m_plain,self.m_key,is16rounds)
        for i in range(len(crypted)):
            if(self.m_crypt+i>len(self.m_out)):
                return
            self.m_out[self.m_crypt+i] = crypted[i]
        for i in range(8):
            if(self.m_crypt+i>len(self.m_out)):
                return
            self.m_out[self.m_crypt+i] = self.m_out[self.m_crypt+i]^self.m_preplain[i]
        for i in range(len(self.m_plain)):
            if(i>len(self.m_preplain)):
                return
            self.m_preplain[i] = self.m_plain[i]
        self.m_precrypt = self.m_crypt
        self.m_crypt+= 8
        self.m_pos = 0
        self.m_header = False
                
    def HashTea(self,binform,bintkye,offset,is16rounds):
        intlen = 0;i = 0;i2 = 0;
        self.m_header = True
        self.m_key = bintkye
        self.m_pos = 0
        self.m_padding = 0
        self.m_crypt = 0
        self.m_precrypt = 0
        intlen = len(binform)
        self.m_pos = (intlen+10)%8
        if(self.m_pos != 0):
            self.m_pos = 8-self.m_pos
        self.m_out = [0 for i in range(intlen+self.m_pos+9+1)]
        self.m_plain[0] = (random.randint(5000,5000)&248)^self.m_pos
        # self.m_plain[0] = (random.randint(5000,5000)&248)^self.m_pos
        for i in range(self.m_pos):
            self.m_plain[i+1] = (random.randint(5000,5000)&255)
            # self.m_plain[i+1] = (random.randint(5000,5000)&255)
        self.m_preplain = [0 for i in range(8)]
        self.m_pos+= 1
        self.m_padding = 1
        while(1):
            if(self.m_pos<8):
                self.m_plain[self.m_pos] = (random.randint(5000,5000))&255
                # self.m_plain[self.m_pos] = (random.randint(5000,5000))&255
                self.m_pos+= 1
                self.m_padding+= 1
            else:
                self.Encrypt8Bytes(is16rounds)
            if(self.m_padding >= 3):break;
        i2 = offset
        while(intlen>0):
            
            if(self.m_pos<8):
                self.m_plain[self.m_pos] = binform[i2-1]
                self.m_pos+= 1
                intlen-= 1
                i2+= 1
            else:
                self.Encrypt8Bytes(is16rounds)
        self.m_padding = 1
        while(self.m_padding<8):
            if(self.m_pos<8):
                self.m_plain[self.m_pos] = 0
                self.m_padding+= 1
                self.m_pos+= 1
            if(self.m_pos == 8):
                self.Encrypt8Bytes(is16rounds)
        return self.m_out
    def decipher(self,bininput,binkey,is16rounds):
        crypted = []
        su = 3816266640;rounds = 0;y = 0;z = 0;a = 0;b = 0;c = 0;d = 0;test = 0;
        y = self.getuint(bininput,1,4)
        z = self.getuint(bininput,5,4)
        a = self.getuint(self.m_key,1,4)
        b = self.getuint(self.m_key,5,4)
        c = self.getuint(self.m_key,9,4)
        d = self.getuint(self.m_key,13,4)
        if(is16rounds):
            rounds = 16
        else:
            rounds = 32
        for i in range(rounds):
            test = ((((y<<4)+c)^(y+su))^((y>>5)+d))
            z-= test
            z = z&4294967295
            test = ((((z<<4)+a)^(z+su))^((z>>5)+b))
            y-= test
            y = y&4294967295
            su-= 2654435769
            su = su&4294967295
        return self.tobytes(y,z)
    def decrypt8bytes(self,_input,offset,intlen):
        for i in range(8):
            if(self.m_contextstart+i>intlen):
                return True
            if(offset+self.m_crypt+i-1 >= len(_input)):
                return False
            self.m_preplain[i] = (self.m_preplain[i])^(_input[offset+self.m_crypt+i-1])
        self.m_preplain = self.decipher(self.m_preplain,self.m_key,True)
        if(len(self.m_preplain) == 0):
            return False
        self.m_contextstart+= 8
        self.m_crypt+= 8
        self.m_pos = 0
        return True
    def UnHashTea(self,binfrom,bintkye,offset,is16rounds):
        o_count = 0;o_m = [];o_intlen = 0;i = 0;i2 = 0;
        self.m_crypt = 0;self.m_precrypt = 0;self.m_key = bintkye;
        o_m = [0 for i in range(offset+7)]
        o_intlen = len(binfrom)
        self.m_preplain = self.decipher(binfrom,self.m_key,True)
        self.m_pos = self.m_preplain[0]&7
        o_count = o_intlen-self.m_pos-10
        for i in range(offset,len(o_m)):
            o_m[i] = 0
        self.m_out = [0 for i in range(o_count)]
        
        self.m_precrypt = 0;self.m_crypt = 8;self.m_contextstart = 8;self.m_pos+= 1;
        self.m_padding = 1
        while(self.m_padding <= 2):
            if(self.m_pos<8):
                self.m_pos+= 1
                self.m_padding+= 1
            if(self.m_pos == 8):
                o_m = binfrom
                self.decrypt8bytes(binfrom,offset,o_intlen)
        # print self.m_out
        i2 = 1
        while(o_count != 0):
            if(self.m_pos<8):
                if(i2 <= len(self.m_out)):
                    if(self.m_pos+1 <= len(self.m_preplain)):
                        if(offset+self.m_precrypt+self.m_pos <= len(o_m)):
                            self.m_out[i2-1] = (o_m[offset+self.m_precrypt+self.m_pos-1])^(self.m_preplain[self.m_pos])
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
                i2+= 1
                o_count-= 1
                self.m_pos+= 1
            if(self.m_pos == 8):
                o_m = binfrom
                self.m_precrypt = self.m_crypt-8
                self.decrypt8bytes(binfrom,offset,o_intlen)
        # print self.m_out
        for i in range(1,8):
            if(self.m_pos<7):
                self.m_pos+= 1
                if(self.m_pos == 8):
                    o_m = binfrom
                    self.decrypt8bytes(binfrom,offset,o_intlen)
        return self.m_out

    def md5_hex(self,data = ""):
        hash = md5.md5()
        hash.update(data)
        hash.digest()
        return hash.hexdigest()

    def md5_bin(self,data = ""):
        hash = md5.md5()
        hash.update(data)
        hash.digest()
        t = hash.hexdigest()
        return tozjj(t)

    def QQTEA(self,data,key):
        # print "key = ",key
        # print "data = ",data
        return self.HashTea(data,key,1,True)
    def UNQQTEA(self,data,key):
        # print "key = ",key
        # print "data = ",data
        if(data == []):
            return []
        if(key == []):
            key = [0 for i in range(16)]
        self.m_precrypt = 0;self.m_crypt = 0;self.m_pos = 0;self.m_padding = 0;self.mout = []
        return self.UnHashTea(data,key,1,True)

class _bin:
    def __init__(self):
        pass
    def flip(self,data):       # 反转字节集
        l = len(data)
        t = []
        for i in range(l):
            t.append(data[l-i-1])
        return t
    def Hex2Bin(self,t):
        return tozjj(t)
        a = []
        for i in range(0,len(t),2):
            try:a.append(int((t[i]+t[i+1]),16))
            except:break
        return a
    def Long2Bin(self,t):
        return self.flip(tozjj(t ,"long" ))
    def Int2Bin(self,t):
        return self.flip(tozjj(t,"int"))
    def Byte2Bin(self,t):
        return tozjj(t,"byte")
    def Short2Bin(self,t):
        return self.flip(tozjj(t,"short"))
    def Bin2Byte(self,t):
        return int(t[0])%256
    def Bin2Hex(self,t):
        return tohex(t);
    def Bin2Int(self,t):
        # t = self.flip(t)
        n = 0
        for i in range(len(t)):
            # print t
            if(t[i] == 0):
                pass
                # t = t-[0]
            else:
                break
        # print "bin2int",t
        for i in range(len(t)):
            t[i] = t[i]%256
            n = n+(255*n+t[i])
            # print n
        return n
    def Bin2Short(self,t):
        t = t[len(t)-2:]
        # print t
        n = 0
        # for i in range(len(t)):
        #     if(t[len(t)-i-1] == 0):
        #         t = t-[0]
        #     else:
        #         break
        # print "bin2int",t
        for i in range(len(t)):
            t[i] = t[i]%256
            n = n+(255*n+t[i])
            # print n
        return n
        try:
            return t[-1]+t[-2]+255*3
        except:
            return t[-1]%256
    def Bin2Long(self,t):
        return self.Bin2Int(t)
    def GetRandomBin(self,l):
        d = []
        for i in range(l):
            d.append(random.randint(0,255))
        return d
class _pack:
    def __init__(self):
        self.m_bin = []
    def Empty(self):
        self.m_bin = []
    def GetAll(self):
        return self.m_bin
    def Len(self):
        return len(self.m_bin)
    def SetBin(self,t):
        self.m_bin+= t
    def SetByte(self,t):
        self.m_bin+= Xbin.Byte2Bin(t)
    def SetData(self,t):
        self.m_bin = t
    def SetHex(self,t):
        t = t.replace(" ","")
        self.m_bin+= Xbin.Hex2Bin(t)
    def SetInt(self,t):
        self.m_bin+= Xbin.Int2Bin(t)
    def SetShort(self,t):
        self.m_bin+= Xbin.Short2Bin(t)
    def SetLong(self,t):
        self.m_bin+= tozjj(t,"int")
    def SetUint(self,t):
        self.SetBin(t)
        # SetBin (到字节集 (Math.ToULong (uint)))
    def SetStr(self,t):
        self.m_bin+= tozjj(t,"str",0)
    def SetToken(self,t):       # 置令牌
        self.SetShort(len(t))
        self.SetBin(t)
class _unpack:
    def __init__(self):
        self.m_bin = []
    def GetAll(self):
        return self.m_bin
    def GetAll_Hex(self):
        return Xbin.Bin2Hex(self.m_bin)
    def GetBin(self,l):
        t = self.m_bin[:l]
        self.m_bin = self.m_bin[(len(self.m_bin)-(len(self.m_bin)-l)):]
        return t
    def GetByte(self):
        t = self.m_bin[:1]
        self.m_bin = self.m_bin[(len(self.m_bin)-(len(self.m_bin)-1)):]
        return Xbin.Bin2Byte(t)
    def GetInt(self):
        t = self.m_bin[:4]
        self.m_bin = self.m_bin[(len(self.m_bin)-(len(self.m_bin)-4)):]
        return Xbin.Bin2Int(t)
    def GetLong(self):
        t = self.m_bin[:8]
        self.m_bin = self.m_bin[(len(self.m_bin)-(len(self.m_bin)-8)):]
        return Xbin.Bin2Long(t)
    def GetShort(self):
        t = self.m_bin[:2]
        # print t
        self.m_bin = self.m_bin[(len(self.m_bin)-(len(self.m_bin)-2)):]
        return Xbin.Bin2Short(t)
    def GetToken(self):
        le = self.GetShort()
        # print le
        t = self.GetBin(le)
        return t
    def Len(self):
        return len(self.m_bin)
    def SetData(self,t):
        self.m_bin = t
    def SetData_Hex(self,t):
        self.m_bin = Xbin.Hex2Bin(t)
Xbin = _bin()
Hash = _hash()
# test：
if __name__  ==  "__main__":
    # print Hash.UNQQTEA([],[103,0,16,89,12,208,21,8,0,191,2,96,81,10,96,196,13,112,215,9,64,84,15])
    # print Xbin.flip([1,2,3,4,5])
    print Xbin.Hex2Bin("522002")
    print Xbin.Bin2Int(Xbin.Hex2Bin("522002"))
    # [124, 26, 95, 0]
    print Xbin.Bin2Int(Xbin.Hex2Bin("5f1a7c"))
    a = 6232700
    print tozjj(a,"int")
    
    print Xbin.Bin2Short([6, 118])
    print Xbin.Bin2Short([300,123,123,332])
    
    print Xbin.Bin2Int([1111, 2, 3, 4])
    print Xbin.Bin2Int([4, 3, 2, 1111])
    print tozjj(67307095,"int")
    print Xbin.Bin2Byte([1111,2,3,4])
    
    tt = Hash.UNQQTEA([ 242, 243, 93, 139, 183, 174, 88, 11, 234, 139, 176, 128, 35, 45, 124, 76, 33, 197, 242, 88, 111, 232, 183, 109, 186, 184, 88, 237, 104, 126, 159, 189, 57, 112, 10, 24, 85, 195, 63, 217, 40, 202, 222, 150, 190, 92, 126, 183, 207, 90, 114, 199, 255, 217, 49, 201, 238, 253, 44, 120, 128, 67, 209, 243, 181, 93, 126, 91, 27, 95, 171, 225, 217, 70, 54, 182, 151, 136, 52, 195, 56, 158, 211, 171, 219, 133, 10, 2, 18, 80, 195, 151, 42, 47, 213, 127, 192, 5, 78, 155, 17, 74, 181, 184, 87, 110, 81, 225, 73, 252, 239, 96, 121, 88, 211, 77, 232, 97, 207, 175, 0, 217, 158, 180, 129, 182, 50, 199, 134, 192, 114, 161, 124, 212, 56, 241, 122, 88, 105, 150, 242, 154, 143, 213, 120, 213, 118, 29, 54, 97, 109, 158, 200, 234, 71, 250, 111, 236, 67, 149, 119, 115, 75, 19, 88, 229, 211, 27, 231, 139, 33, 15, 118, 68, 249, 132, 225, 141, 150, 154, 75, 137, 1, 226 ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])
    print "UNQQTEA = ",len(tt),tt
    print Xbin.Byte2Bin(999)
    print Xbin.Int2Bin(13)
    print Xbin.Short2Bin(13)
    # print Xbin.Hex2Bin("12121")
    print Xbin.Int2Bin(12111)
    print tozjj(1234,"int")
    print tozjj(int(3041507921),"int")
    print tozjj("1axxs","str")
    print "md5_hex:",Hash.md5_hex("a")# 返回十六
    print "md5_bin:",Hash.md5_bin("a")# 返回字节集
    print "UNQQTEA = ",Hash.UNQQTEA(tozjj("qqqqqqqqqqqqqqqq","str"),tozjj("1111111111111111","str"))# UNQQTEA解密
    print "UNQQTEA = ",len(tt),tt
    print Xbin.GetRandomBin(16)
    print "QQTEA = ",Hash.QQTEA(tozjj("qqqqqqqqqqqqqqqq","str"),tozjj("1111111111111111","str"))# QQTEA加密
    print Xbin.Hex2Bin("1234")
    print tozjj("1223","byte")

    
