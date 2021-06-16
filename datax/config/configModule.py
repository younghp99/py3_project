#-*- coding: UTF-8 -*-
'''
purpose：
@author: yhp
'''
configModule={
    "setting":{},
    "job":{
        "setting":{
            "speed": {
            "channel": 2
            }
        },
        "content":{
            "reader":{
                    "name": "",
                    "parameter":{}
            },
            "writer":{
                "name": "",
                "parameter": {}
            }
        }
    }
}
if __name__ == '__main__':
    print(configModule["job"]["content"]["reader"]["name"])
