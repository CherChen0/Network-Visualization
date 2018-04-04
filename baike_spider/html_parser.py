# -*- coding: utf-8 -*-
# coding:utf-8
"""
Created on Thu May 18 18:19:26 2017

@author: cher
"""

from bs4 import BeautifulSoup
#import urlparse
import re
#import string

class HtmlParser(object):
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
       
        links = soup.find_all('a', href=re.compile(r"http://baike.baidu.com/subview/\d+/\d+\.htm"))
        for link in links:
            new_url = link['href']
            #new_full_url = urlparse.urljoin(page_url, new_url)
            new_full_url = new_url
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        res_data['url'] = page_url
        name_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['name'] = name_node.get_text()
        
        nodenode = soup.find('div', class_="star-info-block relations")
        nodes = nodenode.find_all('div', class_="name")
        
        #title_node = soup.find('div', class_="name").find('em')
        str1 = ''
        
        for node in nodes:
            string1=node.get_text()
            string2=node.find('em').get_text()
            l1=len(string1)
            l2=len(string2)
            str1 = str1 + ' ' + string1[0:l1-l2] + ' ' +string2
        
        res_data['relation'] = str1
        res_data['relation'] = unicode (res_data['relation'])
        res_data['name'] = unicode (res_data['name'])
        #print res_data
        return res_data
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
           
        #soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb18030')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup) 
        
        return new_urls, new_data
        