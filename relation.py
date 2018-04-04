# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:53:19 2017

@author: cher
"""

import codecs
import json

fl=open('relation.json', 'w')
#fl=open('../out/map_polyline.js', 'a')

f = codecs.open("new_test.txt",'r')
fileList = f.readlines()
fl.write("[\n")
for fileLine in fileList:  
   y=fileLine.split()
   length = len(y)
   new_length = (length - 2)/2
   data = {}
   data["name"] = y[1]
   for i in range (1,new_length+1):
           data[y[2*i+1]] = y[2*i]
       
   #fl.write(json.dumps(datas))
   fl.write(json.dumps(data,ensure_ascii=False,indent=2))
   fl.write(",\n")
fl.write("]") 
   
f.close()
fl.close()