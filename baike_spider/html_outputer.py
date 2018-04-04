# -*- coding: utf-8 -*-
# coding:utf-8
"""
Created on Thu May 18 18:20:07 2017

@author: cher
"""
import sys
class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html', 'w')
        
        fout.write("<html>")
        #fout.write("<html><meta charset=\"utf-8\" />")
        fout.write("<body>")
        fout.write("<table>")
        type = sys.getfilesystemencoding()
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['name'].encode(type))
            fout.write("<td>%s</td>" % data['relation'].encode(type))
            #
            fout.write("</tr>")
            
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
        
        