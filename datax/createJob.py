#-*- coding: UTF-8 -*-
'''
@author: yhp
'''
from config.configModule import configModule
job_reader_name='txtfilereader'
job_writer_name='txtfilereader'
job_settting_speed_channel=3
file_name='/data/etl/etldata/filename.txt'
fieldDelimiter=','
column_list=''
colunm_list=[]
for i in range(0,5):
    colunm_list.append({"index":i,"type":"string"})
print(colunm_list)
configModule["job"]["setting"]["speed"]["channel"]=job_settting_speed_channel
configModule["job"]["content"]["reader"]["name"]=job_reader_name
configModule["job"]["content"]["writer"]["name"]=job_writer_name
configModule["job"]["content"]["reader"]["parameter"]["path"]=file_name
configModule["job"]["content"]["reader"]["parameter"]["fieldDelimiter"]=fieldDelimiter
configModule["job"]["content"]["writer"]["parameter"]["path"]=file_name
configModule["job"]["content"]["writer"]["parameter"]["fieldDelimiter"]=fieldDelimiter
configModule["job"]["content"]["writer"]["parameter"]["colunm"]=colunm_list

print(configModule)
