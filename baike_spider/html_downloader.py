# -*- coding: utf-8 -*-
# coding:utf-8
"""
Created on Thu May 18 18:19:04 2017

@author: cher
"""
import urllib2
import time
#import socket
#import sys
#import chardet

class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        
        try:
            response = urllib2.urlopen(url, timeout=10)
            htmlCode = response.read()
        
            if response.getcode() != 200:
                return None
        except Exception,e:  
            print 'a',str(e)  
        #time.sleep(1)
        
        #socket.setdefaulttimeout(10)
        return htmlCode.decode('utf-8')