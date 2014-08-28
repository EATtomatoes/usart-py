#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import subprocess
import time
import sys
import USART as us

def getcpuinfo():
    if sys.platform == 'darwin':
        tmp = subprocess.check_output(["top","-i 3","-n 0","-s 2","-l 1","-stats",r"pid,command,cpu,mem"])
        tmp2 = tmp.replace("Processes:","@@Processes:")
        tmp2 = tmp2.split("@@")
        tmp3 = []
        for i in tmp2:
            tmp3.append(i.rstrip())

        print tmp3
        return tmp3

    elif sys.platform == 'linux2':
        tmp = subprocess.check_output(["top","-b","-n 1","-d 2"])
        tmp2 = tmp.replace("Processes:","@@Processes:")
        tmp2 = tmp.split("@@")
        print tmp2
        return tmp2




def getinfo():
    if sys.platform == 'darwin':
        tmp = subprocess.check_output(["top","-i 3","-n 0","-s 2","-l 1"])
        tmp = tmp.rstrip()
        tmp = tmp.split("\n")
        tmp2 = ['system: osx',tmp[0],tmp[2],tmp[3],tmp[6],tmp[8]]

        return tmp2
    elif sys.platform == 'linux2':
        pass


def pushinfo(size=12):
        global us
        us.newpage()
        alist = getinfo()
        for i in alist:
            us.pushLine(i,size)
