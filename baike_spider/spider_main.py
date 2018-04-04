# -*- coding: utf-8 -*-
# coding:utf-8
"""
Created on Thu May 18 18:17:54 2017

@author: cher
"""
from baike_spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlMananger()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
        
    
    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print 'craw %d : %s' %(count, new_url)
                
                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
            
                if count == 1200:
                    print 'done'
                    break
            
                count = count + 1
            
            except:
                print 'craw failed'
            
        self.outputer.output_html()


if __name__== "__main__":
    root_url = "http://baike.baidu.com/subview/9209/6857676.htm"
    obj_spyder = SpiderMain()
    obj_spyder.craw(root_url)