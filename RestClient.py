#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import json
import urllib
#from flask import json ,jsonify
import requests
class RestClient:
    #LMS Emulator
    baseurl = 'https://wh.jandi.com/connect-api/webhook/14114689/0fcffaa35972f44767bb3f12593ecf6f' #local
    header =  {
        "Accept": "application / vnd.tosslab.jandi - v2 + json",
        "Content-Type": "application/json;charset=UTF-8",
    }
    def __init__(self,param):
      pass

    @classmethod
    def SendJandiData(self,data):
        jsonData= {"body":str(data)}
        try:
            print ("url",self.baseurl,"jsonData",jsonData)
            response = requests.post(self.baseurl, data=json.dumps(jsonData), headers=self.header)
            print(response)
            print(response.json())
        except:
            print('%s ', sys.exc_info()[0])

if __name__ == '__main__':
    RestClient.SendJandiData("test")
