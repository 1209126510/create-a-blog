
import sys
import requests
import re
from bs4 import BeautifulSoup
import random
from mylog import MyLog
import pymongo
import time
m1=MyLog()
class crawl(object):
    def __init__(self):
        self.url="http://wufazhuce.com/"
        self.famous_quotes=[]
    def online_suffering(self):
        self.response=requests.get(self.url)
        self.response.encoding = 'utf-8'
        self.response1=self.response.text
        self.soup=BeautifulSoup(self.response1,'lxml')
        self.tag_fq=self.soup.find_all('div',class_='fp-one-cita')
    def remark(self):
        for i in range(0,len(self.tag_fq)):
                self.fq=self.tag_fq[i].text
                self.famous_quotes.append(self.fq)
        self.a=random.randint(0,len(self.famous_quotes)-1)
        self.reply=self.famous_quotes[self.a]
    def chase(self):
        self.online_suffering()
        self.remark()
        return self.reply
    def liebiao(self):
        self.online_suffering()
        self.remark()
        return self.famous_quotes
   