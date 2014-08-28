#!/usr/bin/env  python2.7
# -*- coding: utf-8 -*-
# jarod.py@gmail.com


import USART as us
import extr
import time
import sys

#将下面的tty改为你的电脑上的tty设备名称

tty = "/dev/tty.PL2303-00001004"
rate = 115200






if __name__ == "__main__":
    route = {"pushinfo":"extr.pushinfo()",
             "cmd": "us.acmd(u'%s') "

             }
    us.connect(tty,rate)

    if sys.argv[1] == "pushinfo":
         eval(route[sys.argv[1]]  )

    if sys.argv[1] == "cmd" :
        tmp = ' '.join(sys.argv[2:])
        print tmp
        us.acmd(tmp)
