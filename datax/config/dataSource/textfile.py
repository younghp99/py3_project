#-*- coding: UTF-8 -*-
'''
purpose：文件类型数据源的读取和写入配置
@author: yhp
'''
def reader(path,column_list,fieldDelimiter,skipHeader='false'):
    name='txtfilereader'
    path=[path]
    encoding='UTF-8'
    column_list=column_list
    fieldDelimiter=fieldDelimiter
    reader={
        "name":name,
        "parameter": {
            "path": path,
            "encoding": encoding,
            "column": column_list,
            "fieldDelimiter": fieldDelimiter,
            "skipHeader":skipHeader
        }
    }
    return reader
def writer(path,filename,writeMode,format):
    path=path
    filename=filename
    writeMode=writeMode
    format=format
    writer={
            "name": "txtfilewriter",
            "parameter": {
                "path": path,
                "fileName": filename,
                "writeMode": writeMode,
                "format": format
            }
    }
    return writer
if __name__ == '__main__':
    print(reader('/aa/aa',[{"a":"a"},{"b":"b"}],','))
    print(reader('/aa/aa',[{"a":"a"},{"b":"b"}],',','true'))
    print(writer('/aa/aa','output.txt','truncate','yyyy-MM-dd'))