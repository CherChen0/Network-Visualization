# -*- coding: utf-8 -*-
"""
Created on Thu May 25 19:04:31 2017

@author: cher
"""
import codecs


f = codecs.open("test.txt",'r')
new_f = open("new_test.txt",'w')

fileList = f.readlines()

data = []
i = 0
for fileLine in fileList:  
   y=fileLine.split()
   if y[1] in data:
       print y[1]
   if y[1] not in data:
       new_f.write(fileLine)
       data.append(y[1])
       i = i+1

print i       
f.close()
new_f.close()