#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# jarod.py@gmail.com

import serial ,sys


#串口连接参数
port  = ""
rate  = 115200

#串口屏幕尺寸
width = 220
high = 175

maxx = width - 1
maxy = high - 1



#屏幕光标位置
global current  # 当前光标所处于的行号
current = 0


#初始化函数
def connect(port,rate):
   global ser
   ser = serial.Serial(port,rate)
   cls()
   end()
   print ser
   print "tty connected!\n"



def setup(width,high):
   maxx = width
   maxy = high


# rgb888 to rgb565


def RGB24t16(r,g,b):
    r = bin(r) >> 3
    g = bin(g) >> 2
    b = bin(b) >> 3
    rr = r << 11
    gg = g << 5
    rgb16 = rr + gg + b
    return r,g,b,rgb16





# 计算采用12点阵字符时，字符串需要占用多少水平像素

def widthDS12(strings):
    return len(strings) * 12

def widthDS16(strings):
    return len(strings) * 16

# 计算采用12点阵字符时，字符串需要占用多少行

def lineDS12(strings):
    lines =  len(strings) * 6 / width  #英文用6，汉字用12

    #print lines

    if ((len(strings) * 12 )% width > 0):
        lines = lines + 1

    #print lines
    return lines


def lineDS12W(strings):
    lines =  len(strings) * 12 / width  #英文用6，汉字用12

    #print lines

    if ((len(strings) * 12 )% width > 0):
        lines = lines + 1

    #print lines
    return lines


# 计算采用12点阵字符时，一个包含字符串的列表需要多少行

def lineDS12List(alist):
    count = 0
    for i in alist:
        count += lineDS12(i)
    return count




# 采用size大小的字符，linespace的行间距需要多少行

def linesOfPage(size,linespace = 1):
    tmp = high / (size + linespace)
    return tmp





def pushLine(astring,size,linespace = 1,color = 15):
    global current

    if size == 12:
       countline = lineDS12(astring)
       print 'countline is %d' %countline
       abs12(0,current,maxx,linespace,astring,color)
       step = (12 + linespace) * countline
       print 'step is %d' % step
       current += step
       print "current positoin: %d line" % current
       return  countline

def newpage():
    cls()
    global current
    current =  0



def pushPage(alist,size,linespace,color,delay):
    maxlines = lineOfPage(size,linespace)
    numb = 0
    for i in alist:
       numb += lineDS12(i)
       pass










def utf2gb(astring):
    return astring.encode("gb2312")







#######################################################


def cmd(astring):
    ser.write(astring)

def acmd(astring):
    cmd(astring)
    ser.write("\r\n")

def cls(c = 0):
   acmd("CLS(%d); " % c)


def end():
    cmd("\r\n")

def inf():
    acmd("INF")

def drn(n):
    acmd(n)


def scc(c,n):
    cmd("SCC(%d,%d);" % (c,n))

def ascc(c,n):
    acmd("SCC(%d,%d);" % (c,n))

def sbc(c):
    cmd("SBC(%d);" % c)

def asbc(c):
    acmd("SBC(%d);" % c)



# 12

def ds12(x,y,astring,c):
    cmd("DS12(%d,%d,'%s',%d)" % ( x,y,utf2gb(astring),c))

def ads12(x,y,astring,c):
    acmd("DS12(%d,%d,'%s',%d);" % ( x,y,utf2gb(astring),c))

# 16
def ds16(x,y,astring,c):
    cmd("DS16(%d,%d,'%s',%d);" % (x,y,utf2gb(astring),c))

def ads16(x,y,astring,c):
    acmd("DS16(%d,%d,'%s',%d);" % (x,y,utf2gb(astring),c))

# 32

def ds32(x,y,astring,c):
    cmd("DS32(%d,%d,'%s',%d);" % (x,y,utf2gb(astring),c))

def ads32(x,y,astring,c):
    acmd("DS32(%d,%d,'%s',%d);" % (x,y,utf2gb(astring),c))

# 48

def ds48(x,y,astring,c):
    cmd("DS48(%d,%d,'%s',%d);" % (x,y,utf2gb(astring),c))

def ads48(x,y,astring,c):
    acmd("DS48(%d,%d,'%s',%d);" % (x,y,utf2gb(astring),c))


# 64
def ds64(x,y,astring,c):
    cmd("DS64(%d,%d,'%s',%d);" % (x,y,utf2gb(astring),c))

def ads64(x,y,astring,c):
    acmd("DS64(%d,%d,'%s',%d);" % (x,y,utf2gb(astring),c))


def bs12(x1,y1,x2,lw,astring,c):
    cmd("BS12(%d,%d,%d,%d,'%s',%d);" % (x1,y1,x2,lw,utf2gb(astring),c))

def abs12(x1,y1,x2,lw,astring,c):
    acmd("BS12(%d,%d,%d,%d,'%s',%d);" % (x1,y1,x2,lw,utf2gb(astring),c))


def bs16(x1,y1,x2,lw,astring,c):
    cmd("BS16(%d,%d,%d,%d,'%s',%d);" % (x1,y1,x2,lw,utf2gb(astring),c))

def abs16(x1,y1,x2,lw,astring,c):
    acmd("BS16(%d,%d,%d,%d,'%s',%d);" % (x1,y1,x2,lw,utf2gb(astring),c))




def spot(x,y,c):
    cmd("PS(%d,%d,%d);" % (x,y,c))

def aspot(x,y,c):
    acmd("PS(%d,%d,%d);" % (x,y,c))

def line(x1,y1,x2,y2,c):
    cmd("PL(%d,%d,%d,%d,%d)" % (x1,y1,x2,y2,c))

def aline(x1,y1,x2,y2,c):
    acmd("PL(%d,%d,%d,%d,%d)" % (x1,y1,x2,y2,c))

def box(x1,y1,x2,y2,c):
    cmd("BOX(%d,%d,%d,%d,%d)" % (x1,y1,x2,y2,c))


def abox(x1,y1,x2,y2,c):
    acmd("BOX(%d,%d,%d,%d,%d)" % (x1,y1,x2,y2,c))


def boxf(x1,y1,x2,y2,c):
    cmd("BOXF(%d,%d,%d,%d,%d);" % (x1,y1,x2,y2,c))

def aboxf(x1,y1,x2,y2,c):
    acmd("BOXF(%d,%d,%d,%d,%d);" % (x1,y1,x2,y2,c))

def pic(x,y,c):
    cmd("PIC(%d,%d,%d);" % (x,y,c))

def apic(x,y,c):
    acmd("PIC(%d,%d,%d);" % (x,y,c))

def cir(x,y,r,c):
    cmd("CIR(%d,%d,%d,%d);" % (x,y,r,c))

def acir(x,y,r,c):
    acmd("CIR(%d,%d,%d,%d);" % (x,y,r,c))


def spg(n):
    cmd("SPG(%d);" % n)


def aspg(n):
    acmd("SPG(%d);" % n)
