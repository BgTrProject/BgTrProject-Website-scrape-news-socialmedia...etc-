# import os
# import bs4
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np
# import os
# import time
# import urllib.request
# import re
# import urllib3
# from pandas import DataFrame
# import csv
# import datetime
# from datetime import datetime, timedelta
# import os
# import csv
# import concurrent
# import multiprocessing
# from multiprocessing import pool
# import io
# from pprint import pprint
#
#
# def headermenuitemfinder(link):
#   category_array = []
#   b = "/"
#   lnk = ""
#   req = requests.get(link)
#   soup = BeautifulSoup(req.content, "lxml")
#   # title=soup.find("ul",attrs={"class":"navbar-nav"}).findAll('li')
#   title = soup.findAll("a")  # ,attrs={"class":"main_nav__link"})
#   s = 0
#   for i in title:
#
#     j = i.get("href")
#     if (s == 16):
#       break
#     if (j.startswith("/category")):
#       b = (i.get("href"))
#       s += 1
#       lnk = ("{}{}{}".format("https://www.segabg.com", b, "?page=1"))
#       category_array.append(lnk)
#   return category_array
#
#
# def is_exist(self, link, c):
#   # print(link)
#   count = c
#   r = requests.get(link)
#   soup = BeautifulSoup(r.content, 'html5lib')
#   art = soup.findAll("div", attrs={"class": "article"})
#   # print(count)
#   if len(art) > 1:
#     if count < 10:
#       # print(count)
#       count += 1
#       new_link = "{}{}".format(link[:-1], count)
#       return self.is_exist(new_link, count)
#     elif count < 100:
#       # print(count)
#       count += 1
#       new_link = "{}{}".format(link[:-2], count)
#       return self.is_exist(new_link, count)
#     elif count < 1000:
#       # print(count)
#       count += 1
#       new_link = "{}{}".format(link[:-3], count)
#       return self.is_exist(new_link, count)
#     # return True
#   else:
#     return count - 1
#
# def page_count_finder(link):
#   s=1
#   for i in range(1000):
#     lnk=link[:-1]
#     print("{}{}".format(lnk,s))
#     if(s==5):
#       break
#     s+=1
#
# def all_page_links(categories_links):
#   All_pages_links=[]
#   for i in categories_links:
#     category_pages_count=is_exist(i,1)
#     for j in range(len(category_pages_count)):
#       All_pages_links.append("{}{}".format(categories_links[i-1],j+1))
#       # print(All_pages_links)
#   return All_pages_links
#
# #
# # def dateCreator(d1,d2):
# #   technology = []
# #   # uk-news  coronavirus-outbreak   environment/climate-crisis
# #   # uk/environment   science   global-development  uk/technology  uk/business
# #   category = ['uk-news','science','coronavirus-outbreak','environment/climate-crisis','uk/environment','global-development','uk/technology','uk/business']
# #   # ser_date = pd.Series(pd.date_range('19990101', periods=8400))
# #   d1=date(d1)
# #   d2=date(d2)
# #   delta=int(d2-d1)
# #   ser_date = pd.Series(pd.date_range(d1, periods=8400))
# #   link = "https://www.theguardian.com/"
# #   for i in category:
# #     for j in range(0,delta):
# #       dateEnd  = ser_date[j].strftime("/%Y/%b/%d/all")
# #       technology.append("{}{}{}".format(link,i,dateEnd))
# #   return technology
# #
# #
# #
# #
# # from datetime import date
# # d0 = date(2017, 8, 18)
# # d11 = date(2017, 10, 26)
# # delta = d11 - d0
# # print(delta.days)
# #
# # dates = dateCreator(d0,d1)
# # for x in dates:
# #   print(x)
# #   # with open("AllMainLinks.txt", 'a') as file:
# #   #   file.write(x+'\n')
# # print("Başarılı")
# #
# #
# #
# # technology = []
# # # uk-news  coronavirus-outbreak   environment/climate-crisis
# # # uk/environment   science   global-development  uk/technology  uk/business
# # category = ['uk-news','science','coronavirus-outbreak','environment/climate-crisis','uk/environment','global-development','uk/technology','uk/business']
# # # ser_date = pd.Series(pd.date_range('19990101', periods=8400))
# # d1=d0
# # d2=d11
# # delta=d2-d1
# # h=delta.total_seconds()
# # z=int(h/(3600*24))
# # print(z)
# # ser_date = pd.Series(pd.date_range(d1, periods=8400))
# # link = "https://www.theguardian.com/"
# # for i in category:
# #   for j in range(0,z):
# #
# #     dateEnd  = ser_date[j].strftime("/%Y/%b/%d/all")
# #     technology.append("{}{}{}".format(link,i,dateEnd))
# # print(technology)
# # # return technology
#
#
#
# # import os
# # from webapp.newspaper_codes.dwnews import dwnews
# # date1 = "11/11/2011"
# # date2 = "12/12/2020"
# # category = "science"
# # fname="fff"
# #
# # # fname = request.GET.get("newspaper_filename")  # use as directory
# # cl_names_all = 'dwnews'
# #
# # fn = []
# # link_list = []
# # content_list = []
# # file_list = []
# #
# # cl = cl_names_all.split(",")
# # desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
# # print(desktop)
# # way = "{}{}{}/".format(desktop[:-7], "websites/rubic/webapp/g_upload/", fname)
# # print(way)
# #
# # try:
# #     os.makedirs(way, exist_ok=True)
# #     print("Directory '%s' created successfully" % fname)
# # except OSError as error:
# #     newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname
# #
# #     # return newspaper_result
# #
# # for i in cl:
# #     h_link = "{}{}_{}_link.txt".format(way, fname, i)
# #     h_content = "{}{}_{}_content.txt".format(way, fname, i)
# #     link_list.append(h_link)
# #     content_list.append(h_content)
# #
# #     file_list.append(h_link)
# #     file_list.append(h_content)
# #
# #     h = "{}".format(i.strip())
# #     print(h)
# #     print("--------hhhhhhh ---------------")
# #     fn.append(h)
# # ss = []
# # for i in range(len(cl)):
# #     print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
# #     print(i)
# #
# #     ii = '{}={}({},{},"{}","{}","{}")'.format(cl[i], cl[i], date1,date2,category,fn[i], fname)
# #     print(ii)
# #     print("zzzzzzzzzzzzzzzzzzzzzzzz")
# #     ss.append(ii)
# # zeta = []
# # sayac = 0
# # for i in ss:
# #     print(i)
# #     print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")
# #     exec(i)
# #     d_link = "{}".format(link_list[sayac])
# #     print("---------------------------------- dlink---------")
# #     print(d_link)
# #     print("???????????????????????")
# #
# #     z = i.split("=")
# #     print(z)
# #     zet = "{}{}".format(z[0], ".main()")
# #     zeta.append(zet)
# #     print("zeeeeeeeeeeettttttttttt")
# #     print(zet)
# #     exec(zet)
# #     d_content = ("{}".format(content_list[sayac]))
# #     print(" ***************** d_content ****************")
# #     print(d_content)
# #     print(" ***************** d_content ****************")
# #     # zipped_file = zipFiles(d_content)
# #     # download_file_g(d_content)
# #     sayac += 1




#======================== zip download ====================================

# desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
# print(desktop)
# way = "{}{}{}/".format(desktop[:-7], "websites/rubic/webapp/g_upload/", fname)
# print(way)
#
# try:
#     os.makedirs(way, exist_ok=True)
#     print("Directory '%s' created successfully" % fname)
# except OSError as error:
#     newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname
# file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
# print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
# print(file_path)
# zf = "{}/{}".format(file_path, fname)
# print(zf)
# print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
#
# shutil.make_archive(zf, 'zip', file_path)
# zf_s = "{}{}".format(zf, '.zip')
# print(zf_s)
#
# file = open(zf_s, 'rb')
# response = FileResponse(file)
# response['Content-Type'] = 'application/octet-stream'
# response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)
# return response