# -*- coding: utf-8 -*-

import os
import os.path
import pickle
import  struct
import sys
import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])
filename = "E:\\project_code\\py3_project\\data\\10004SMYZT_zBank_20210324_FBJ.txt"
filename_new="E:\\project_code\\py3_project\\data\\10004SMYZT_zBank_20210324_FBJ.dmp"


fileNew=open(filename_new,'wb')
file=open(filename,'r')
lines=file.readlines()
for line in lines:
    curLine=line.split(' ')
    for i in range(len(curLine)):
        if len(curLine[i])==0:
            continue
        print(curLine[i])
        parsedata = struct.pack('f',curLine[i])
        fileNew.write(parsedata)
    fileNew.write('\n')

fileNew.close()
file.close()
