from encodings import utf_8
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import time
import urllib.request
import re
import urllib3
from pandas import DataFrame
import csv
import datetime
from datetime import datetime, timedelta, date
import concurrent
import concurrent.futures
from concurrent.futures.thread import ThreadPoolExecutor

links = []
linkNews = []
newsLinks = []


class takvim: 
    
    def __init__(self,keyword,filname,dirname,**kwargs):
        # self.date1=date1
        # self.date2=date2
        self.dirname = dirname
        self.links=[]
        self.linkNews=[]
        self.newsLinks=[]
        self.filname=filname


        self.keyword=keyword
        # self.url = url
        self.count="2"
        print(self.keyword)
        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamad─▒")
        h=os.getcwd()
        print("?????????????????")
        print(self.filname)
        filname2 = self.filname
        if (h.startswith("/home")):
            try:
                # ff = str(filname)
                # self.filname = desktop + "/" + filname
                ff = str(filname)
                print("===========================================")
                print(ff)
                print("===========================================")
                # self.filname = desktop + "/" + filname
                self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,
                                                                                             self.dirname) + ff  # +"/"+ff

                self.content_filname = self.filname + "_content.txt"
                self.link_filname = self.filname + "_link.txt"
                print(self.link_filname)
            except:
                pass
        else:
            ff = str(filname)
            self.filname = desktop + "//" + filname2
            self.content_filname = self.filname + "_content.txt"
            self.link_filname = self.filname + "_link.txt"
            print(self.link_filname)
            
            
    
    def date_creator(self,count,keyword):
        print("datecreator")
        count=int(count)
        print(type(count))
        # print(count) 33333333333333333333
        #https://www.takvim.com.tr/get_arama_arsiv_futbol/1   
        # count = 1
        for i in range(1, int(count)+1): 
            lnk = "https://www.takvim.com.tr/get_arama_arsiv_"+keyword+"/{}".format(str(i)) 
            self.links.append(lnk)
            print(lnk)   
        return self.links
    
    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def getAllLinks(self,url):
        # print(keyword) 
        # print("getalllinks") 44444444444444444
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        count=0
        for a in soup.find_all('a', href=True):
            link = a['href']
            
            if len(link)>15:
                count+=1
                if (count%3==0):
                    linkNews.append(link)
                    href = "https://www.takvim.com.tr"+link
                    print(href)
        # print(linkNews)

                    with open(self.link_filname, "a", encoding="utf-8") as file:
                        # print(link)
                        file.write(href+"\n")
        return "Yazd─▒r─▒l─▒yor"
    
    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def creator(self,url):
            # print(url +"++++++++++++++++++++")
            # print("girdi")
            html = requests.get(url).content  
            # print(html) 
            soup = BeautifulSoup(html, "html.parser")
            # print(soup)
            title = soup.find("h1").getText()
            print(title)
            content_array = soup.find("div", {"id": "contextual"}).getText()
            content_array = content_array.split()
            content_string = ""
            for w in content_array:
                content_string = content_string+" "+w
            print(content_string)
            date = soup.find("div", {"class": "infoBox"}).getText().split()   
            # print(date)    
            # date = date.split()
            date = date[1]
            date = date.replace('.', '-')
            print(date)
            
            # w_data = url+";"+date+";"+title+";"+content_string
            w_data="{};{};{};{}".format(url,date,title,content_string)
            #write_to_txt(w_data)
            with open(self.content_filname, 'a',encoding='utf-8') as file: 
                
                file.write(w_data+'\n')

            return
                
    # //////////////////////////////////////////////////////////////////////////////////////////////////
    def getpagecount(self,keyword):
            print("Getpagecount") 
            print(keyword)
            # https://www.takvim.com.tr/arama/arsiv/korona 
            url = "https://www.takvim.com.tr/arama/arsiv/"+keyword
            html = requests.get(url).content
            soup = BeautifulSoup(html, "html.parser")
            list = soup.find("div",{"class" : "searchTitle"}).find("span").getText()
            # print(list)
            count = list 
            count = count.replace('.', '')
            print(count)        
            count=int(count)
            if (count % 10 != 0):
                count = count / 10
                
            # print(count)
            else:
                count = count / 10
                count -= 1
            print(count)
       
            return count
    #//////////////////////////////////////////////////////////////////////////////////////////////////
    def main(self):
        # takvim.creator("https://www.takvim.com.tr/spor/2022/03/23/a-milli-futbol-takimi-2022-dunya-kupasi-yolunda-portekiz-deplasmaninda",keyword)
        count = takvim.getpagecount(self,self.keyword)
        
        self.count = int(count)
        counter = round(int((self.count / 10) + 1))
        print(counter)

        allLinks = takvim.date_creator(self,count,self.keyword)

        for i in range(counter):
            self.getAllLinks(allLinks[i].strip())
            print("get all link........takvim........")

        print(self.link_filname)

        # t1 = time.time()
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res = [execut.submit(
        #         takvim.getAllLinks, i.strip(),self.keyword) for i in allLinks]
        # print(time.time()-t1)
        
        with open(self.link_filname,'r',newline='') as f:
            for i in f.readlines():    
                self.newsLinks.append(i)

        print("-----------------------")
        print(self.content_filname)
        print(self.link_filname)
        print("-------------------------")
        # # for i in self.newsLinks:
        # #     print(i.strip())
        #
        for i in self.newsLinks[:5]:
            self.creator(i.strip())

        # t3 = time.time()
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res = [execut.submit(
        #         takvim.creator, i.strip(),self.keyword) for i in self.newsLinks]
        # print(time.time()-t3)
        #
        print("Successfully!")
        

