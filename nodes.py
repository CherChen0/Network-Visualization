# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:37:09 2017

@author: cher
"""

import codecs
import json

fl=open('nodes.json', 'w')
#fl=open('../out/map_polyline.js', 'a')

f = codecs.open("new_test.txt",'r')
fileList = f.readlines()
fl.write("[\n")
for fileLine in fileList:  
   y=fileLine.split()
   data = {}
   data["name"]=y[1]
   data["url"]=y[0]
   fl.write(json.dumps(data,ensure_ascii=False,indent=0))
   fl.write(",")
   #fl.write("{\"name\":\"" + y[1] + "\",\"url\":\"" + y[0] + "\"},")
   fl.write("\n")
fl.write("]")   

f.close()
fl.close()