# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:50:41 2017

@author: cher
"""
import json
import sys

reload(sys) 
sys.setdefaultencoding('utf-8')
f = open('relation.json', 'r')
relations_data = json.load(f)
f.close()


fl=open('relation11.json', 'w')
#fl=open('../out/map_polyline.js', 'a')
fl.write("[\n")

for x in relations_data:  
    list_keys = x.keys()
    length = len(list_keys)
    for i in range(0 , length):
        data = {}
        if list_keys[i] != "name":
            data["node1"] = x["name"]
            data["node2"] = list_keys[i]
            data["relation"] = x[list_keys[i]]
            fl.write(json.dumps(data,ensure_ascii=False,indent=2))
            fl.write(",\n")
       
fl.write("]") 
   
fl.close()