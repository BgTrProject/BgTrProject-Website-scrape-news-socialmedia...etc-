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


class dailyHurriyet:
    
    def __init__(self,keyword,filname,dirname,**kwargs):
        # self.date1=date1
        # self.date2=date2
        self.dirname=dirname
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
                ff = str(filname)
                # self.filname = desktop + "/" + filname
                self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,self.dirname) + ff  # +"/"+ff
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
            
        #/////////////////////////////////////////////////////////////////////////////////    

    def date_creator(self,count, keyword):
        count=int(count)
        # print(count)
        # https://www.hurriyetdailynews.com/search/corona?p=2
        for i in range(1, int(count)+1):
            lnk = "https://www.hurriyetdailynews.com/search/" + \
                keyword+"?p={}".format(str(i))
            self.links.append(lnk)
            # print(lnk)
        return self.links

    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def getAllLinks(self,url):
        # print(keyword)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        list = soup.find_all("div", {"class": "col-md-4 col-sm-4"})
        for i in list:
            href = i.find("a").get("href")
            if href.startswith("https://www.hurriyetdailynews.com"):
                # print(href)
                # print("???????????????????????")
                pass
            else:
                # href = "https://www.hurriyetdailynews.com"+href
                # print("=======================")
                # print(href)
                print(self.link_filname)
                href_="{}{}".format("https://www.hurriyetdailynews.com",href)
                with open(self.link_filname, "a", encoding="utf-8") as file:
                    file.write(href_+"\n")
                    # print(href)
        return "Yazd─▒r─▒l─▒yor"

    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def creator(self,url):
        print("------------------")
        print(url)
        print("*******")
        print("------------------")
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("div", {"class": "content"}).find(
            "h1").getText()  # T─░TLE Tamam
        date = soup.find("div", {"class": "content-info"}).find_all("ul")
        date = date[1].getText()

        date = date[:-9]
        date = date.strip()

        content = soup.find("div", {"class": "content"}).find_all("p")
        content_string = ""
        categori = "Science"

        for i in content:
            i = i.getText().replace(" ", " ")
            z = " ".join(i.split())
            content_string += z

        sentence = "{} ; {} ; {} ; {} ; {}".format(
            url, date, categori, title, content_string)
        print(date)
        with open(self.content_filname, "a", encoding="utf-8") as file:
            file.write(sentence + "\n")

            # //////////////////////////////////////////////////////////////////////////////////////////////////
    def getpagecount(self,keyword):
        print("++++++++++++++++")
        # https://www.hurriyetdailynews.com/search/corona?p=2
        url = "https://www.hurriyetdailynews.com/search/"+str(keyword)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        count = soup.find("p", {"class": "search-result-summary"}).getText()
        count = count.replace('.', '')
        # print(count)
        count = count.split(" ")
        count = count[1]

        count = int(count)
        try:
            if (count > 2550):
                count = 2550

            if (count % 51 != 0):
                count = count / 51
                # print(count)
                count += 1
                # print(count)
            else:
                count = count / 51
                # print("devam")
        except:
            count=51

        return count
    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def main(self):
        print("*********************")
        print(self.keyword)

        count = dailyHurriyet.getpagecount(self,self.keyword)
        print(count)
        print("sssssssssssssssssssssssssssssssssssssss page ssssssssssssssssss")
        self.count = int(count)
        counter = round(int((self.count / 10) + 1))
        print(counter)

        allLinks = dailyHurriyet.date_creator(self,count,self.keyword)
        # for i in alllinks[:5]:
        #     print(i)
        #     self.getAllLinks(i)
        # print("-------------------------------------------")

        t1 = time.time()
        for i in range(counter):
            self.getAllLinks(allLinks[i].strip())
            print("get all linksssssssssssssssssssssssssssssssss")

        # print(self.link_filname)
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res = [execut.submit(self.getAllLinks, i.strip()) for i in alllinks[:3]]
        # print(time.time()-t1)

        with open(self.link_filname,'r',newline='',encoding="utf-8") as f:
            for i in f.readlines():    
            # reader=csv.reader(f)
                i = i.strip("\n")
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


        # t2=time.time()
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res=[execut.submit(self.creator,i.strip()) for i in self.newsLinks]
        # print(time.time()-t2)

        print("Successfully!")
# if __name__ == "__main__":
#     dailyHurriyet.main()