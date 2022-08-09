import en_core_web_sm
import spacy
from spacy.lang.en.examples import sentences

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
nlp=en_core_web_sm.load()

from django.shortcuts import render,HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect
import plotly.express as px
import os
import sys


import praw
from newsplease import NewsPlease
import csv
import json
import json_normalize
from pycode.news import newspaper
import requests
import csv
import json_normalize
import pandas as pd
import dtale
import time
from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time
import numpy as np
from tweepy import *
import tweepy as tw
import shutil
from codes.vatan import *
from codes.takvim import *
from codes.turkiyeGazetesi import *
from codes.sabah import *
from codes.haberler import *
# from codes.haberler2 import *
# from webapp.newspaper_codes.dwnews import *
from newspaper_codes.dwnews import *
from newspaper_codes.guardian import *
from newspaper_codes.independent import *
from newspaper_codes.dailymail import *
from newspaper_codes.dailysabah import *



from codes.dailySabah import *
from codes.dailyHurriyet import *


from newspaper_codes.dnevnik import *
from newspaper_codes.trud import *
from newspaper_codes.bgnes import *
from newspaper_codes.banker import *
from newspaper_codes.sega import *





from newspaper_codes.ensonhaber import *
from newspaper_codes.sozcu import *
from newspaper_codes.haberler import *
from newspaper_codes.evrensel import *
from newspaper_codes.hurriyet import *
from newspaper_codes.memurlar import *
from newspaper_codes.turkiye import *
from newspaper_codes.sabah import *
from newspaper_codes.milli import *
from newspaper_codes.duvar import *
from newspaper_codes.odatv4 import *
from newspaper_codes.cumhuriyet import *
import requests
import logging

import wget
from django.conf import settings
from django.http import HttpResponse, Http404
from django.http import FileResponse
from pycode.google import google_search
from pycode.google6 import google_search6
from pycode.bing import Bing
from pycode.google7 import google_search7
from pycode.google8 import google_search8

import mimetypes
from io import StringIO
import zipfile


from facebook_scraper.utils import *
from facebook_scraper.page_iterators import *
from facebook_scraper.fb_types import *
from facebook_scraper.facebook_scraper import *
from facebook_scraper.extractors import *
from facebook_scraper.exceptions import *
from facebook_scraper.constants import *
from facebook_scraper.__main__ import *
from facebook_scraper.__init__ import *

from facebook_scraper.facebook_scraper import *
from django.shortcuts import render,HttpResponse
# from facebook_scraper.facebook_credentials.txt import *
import os
import tweepy as tw
import pandas as pd
import snscrape.modules.twitter as sntwitter
from django.http import HttpResponse
import csv

import pandas as pd
import ast
import time
from datetime import datetime
import requests
import logging




# ================================ elastic Search{{{{{{{{{{{{{{{{{

#
# from django.shortcuts import render
#
# # Create your views here.
# from django.http import JsonResponse
# import requests
# import json
# from home.models import *
#
# from .documents import *
# from .serializers import *
#
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     CompoundSearchFilterBackend
# )
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     OrderingFilterBackend,
# )
#
#
# def generate_random_data():
#     url = 'https://newsapi.org/v2/everything?q=apple&from=2021-04-23&to=2021-04-23&sortBy=popularity&apiKey=827705eea42e455cba8bf4afafc7da90'
#     r = requests.get(url)
#     payload = json.loads(r.text)
#     count = 1
#     for data in payload.get('articles'):
#         print(count)
#         ElasticDemo.objects.create(
#             title=data.get('title'),
#             content=data.get('description')
#         )
#
#
# def index(request):
#     generate_random_data()
#     return JsonResponse({'status': 200})
#
#
# class PublisherDocumentView(DocumentViewSet):
#     document = NewsDocument
#     serializer_class = NewsDocumentSerializer
#     lookup_field = 'first_name'
#     fielddata = True
#     filter_backends = [
#         FilteringFilterBackend,
#         OrderingFilterBackend,
#         CompoundSearchFilterBackend,
#     ]
#
#     search_fields = (
#         'title',
#         'content',
#     )
#     multi_match_search_fields = (
#         'title',
#         'content',
#     )
#     filter_fields = {
#         'title': 'title',
#         'content': 'content',
#     }
#     ordering_fields = {
#         'id': None,
#     }
#     ordering = ('id',)


# ==============================endo of elastic Search }}}}}}}}}}}}}}}}}}}}}}


# outfile = StringIO.StringIO()
from newsplease import NewsPlease
import asyncio
from directory_downloader import DDownloader
from django.shortcuts import render

from subprocess import Popen
from signal import SIGINT

import time
import json
# from .service import Regression
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse


class MainView(View):

    def get(self, request):
        if "submit" in request.GET:
            return redirect("result")
        return render(request, './templates/index5.html')


class ResultView(View):

    def get(self, request):
        return render(request, './templates/results.html')

    @staticmethod
    def ajax_view(request):
        start_time = time.time()
        # R = Regression()
        R=newspaper_search_all()

        # rmse = R.get_rmse()
        context = {"rmse": newspaper_search_all(), "time": time.time() - start_time}
        data = json.dumps(context)
        return HttpResponse(data, content_type="application/json")





from signal import SIGTERM,SIGKILL
from psutil import process_iter
def kill(request):
    # start the process
    # p = Popen(['python', 'manage.py', 'runserver 0.0.0.0:8004'])
    # p.send_signal(SIGINT)
    # p.wait()
    # exec('killall -u')
    h=process_iter()
    for i in h:
        i.send_signal(SIGTERM)
        continue
    result_k_s = "the process stopped by you"  # {} results".format("z")
    print(result_k_s)
    return render(request, 'index5.html', {"result_k_s": result_k_s})

    pass


def open_dtale(request):
    odt = request.GET.get("odt")
    print(odt)
    h=dtale.show()
    zz="85.105.63.196:40000/dtale/popup/upload"
    aa="bilgi-ms-7b98:40000/dtale/main/"
    # response=redirect(reversed(h.build_main_url(zz)))
    h.build_main_url(zz)

    response=redirect(h.build_main_url(zz))
    response=None
    result_c_s = "dtale opened completed "  # {} results".format("z")
    print(result_c_s)
    return render(response, 'index5.html', {"result_c_s": result_c_s})

    # filepath = zz
    # print(filepath)
    # # Open the file for reading content
    # # path = open(filepath, 'rb')
    # # Set the mime type
    # mime_type, _ = mimetypes.guess_type(filepath)
    # # Set the return value of the HttpResponse
    # response = HttpResponse(filepath, content_type=mime_type)
    # # Set the HTTP header for sending to browser
    # # response['Content-Disposition'] = "attachment; filename=%s" % ""
    # return response


    #
    # print(h)
    # h.build_main_url(zz)
    #
    # response=redirect(h.build_main_url(zz))
    # return response



# Define function to download pdf file using template
# def download_file(request, filename=''):
#     if filename != '':
#         # Define Django project base directory
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         # Define the full file path
#         filepath = BASE_DIR + '/upload/' + filename
#         # Open the file for reading content
#         path = open(filepath, 'rb')
#         # Set the mime type
#         mime_type, _ = mimetypes.guess_type(filepath)
#         # Set the return value of the HttpResponse
#         response = HttpResponse(path, content_type=mime_type)
#         # Set the HTTP header for sending to browser
#         response['Content-Disposition'] = "attachment; filename=%s" % filename
#         # Return the response value
#         return response
#     else:
#         # Load the template
#         return render(request, 'index.html')

#
def download_file(request,filename):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define text file name
        print(BASE_DIR)
        filename = filename
        print(filename)
        # Define the full file path
        filepath = BASE_DIR  +'/upload/'+ filename
        print(filepath)
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        # df=pd.read_csv(filepath)
        h = dtale.show()
        # z=redirect(h.build_main_url())
        z = redirect(h.open_browser())
        z
        # resp

        # df = pd.read_csv(filname8)
        # d = dtale.show(df)
        # d.open_browser()
        return response

        # return resp
    else:
        pass
        # return render(request, 'index.html')

################################### download file_g ###########################

def download_file_g(filename):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define text file name
        print(BASE_DIR)
        filename = filename
        print(filename)
        # Define the full file path
        filepath = BASE_DIR  +'/g_upload/'+ filename
        print(filepath)
        print("---------------filepathhhhhhhhhhhhhhhhh----------------")
        #
        # r = requests.get(filepath, allow_redirects=True)
        # open(filepath, 'wb').write(r.content)

        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # response
        # Return the response value
        # df=pd.read_csv(filepath)
        # h = dtale.show()
        # # z=redirect(h.build_main_url())
        # z = redirect(h.open_browser())
        # z
        # resp

        # df = pd.read_csv(filname8)
        # d = dtale.show(df)
        # d.open_browser()
        return response

        # return resp
    else:
        pass
        # return render(request, 'index.html')
############--------------end of download file_g -------------------------------

################################## complex snscrape #################################

def complex_snscrape(request):
    tweet_count = request.GET.get("tweet_count")
    since_date = request.GET.get("since_date")
    text_query = request.GET.get("text_query")
    fromuser = request.GET.get("fromuser")
    lang = request.GET.get("lang")
    filname = request.GET.get("filname")
    fl=str(filname)
    filname = fl + ".csv"
    mm=filname
    # result_c_s="bos"


    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h = os.getcwd()
    filname2 = filname
    if (h.startswith("/home")):
        try:
            ff = str(filname)
            filname = desktop[:-7] + "websites/rubic/webapp/upload/" + ff
            os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} lang:{}"> {}'
                      .format(tweet_count, since_date, text_query, fromuser, lang, filname))
            filname8 = str(mm)
            print("aaaaaaaaaaaaaaaaaaaaaa")
            raw_tweets = pd.read_json(filname, lines=True)
            raw_tweets.to_csv(filname, index=False)
            # print("bbbbbbbbbbbbbbb")
            # # result3 = "successfully completed with {} results".format(len(raw_tweets))
            # users = json_normalize(raw_tweets['user'])
            # print("ccccccccccccccccccccccccccc")
            # users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
            # users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
            # # Create DataFrame and remove duplicates
            # users = pd.DataFrame(users)
            # print("ddddddddddddddddddddddddd")
            # # users.drop_duplicates(subset=['userId'], inplace=True)
            # # Transform 'raw_tweets' DataFrame
            # # Add column for 'userId'
            # user_id = [user['id'] for user in raw_tweets['user']]
            # raw_tweets['userId'] = user_id
            # # Remove less important columns
            # cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
            #         'quoteCount']
            # tweets = raw_tweets[cols]
            # tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
            # cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
            #         'location']
            # use = users[cols]
            # twts = use.merge(tweets, on='userId')
            # twts.to_csv(filname, index=False)







            print(filname)
            print(filname8)
            print("----------------------------------")
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filepath = BASE_DIR + '/upload/' + filname8
            print(filepath)
            # Open the file for reading content
            path = open(filepath, 'rb')
            # Set the mime type
            mime_type, _ = mimetypes.guess_type(filepath)
            # Set the return value of the HttpResponse
            response = HttpResponse(path, content_type=mime_type)
            # Set the HTTP header for sending to browser
            response['Content-Disposition'] = "attachment; filename=%s" % filname8
            h = dtale.show()
            h.main_url()
            return response
            # download_file(filname8)
            # raw_tweets = pd.read_json(filname8, lines=True)
            # raw_tweets.to_csv(filname8,index=None)
            # df = pd.read_csv(filname8)
            # d = dtale.show(df)
            # d.open_browser()
            # h = dtale.show()
            # redirect(h.main_url())



            # return response
            # df = pd.read_csv('C:\\Users\chs\Downloads\asd.csv')
            # df = px.data('C:\\Users\chs\Downloads\asd.csv')
            # df = pd.read_csv('Home/bilgi/Downloads/asd.csv')
            # df = px.data('Home/bilgi/Downloads/asd.csv')
            # d = dtale.show(df)
            # d.open_browser()
            result_c_s = "successfully completed with"# {} results".format("z")
            print(result_c_s)
            return render(response, 'index5.html', {"result_c_s": result_c_s})


        except:
            print("pathway problem occurred for complex search . Please check your pathway")
            pass
    else:
        print("nanay")
        # desktop2 = desktop.replace("Desktop", "Masaüstü")
        # ff = str(filname2)
        # filname2 = desktop2 + "//" + filname2
        # os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} lang:{}"> {}'
        #           .format(tweet_count, since_date, text_query, fromuser, lang, filname))
        #
        # raw_tweets = pd.read_json(filname2, lines=True)
        # # result3 = "successfully completed with {} results".format(len(raw_tweets))
        # users = json_normalize(raw_tweets['user'])
        # users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
        # users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
        # # Create DataFrame and remove duplicates
        # users = pd.DataFrame(users)
        # # users.drop_duplicates(subset=['userId'], inplace=True)
        # # Transform 'raw_tweets' DataFrame
        # # Add column for 'userId'
        # user_id = [user['id'] for user in raw_tweets['user']]
        # raw_tweets['userId'] = user_id
        # # Remove less important columns
        # cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
        #         'quoteCount']
        # tweets = raw_tweets[cols]
        # tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
        # cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
        #         'location']
        # use = users[cols]
        # twts = use.merge(tweets, on='userId')
        # twts.to_csv(filname2, index=False)
        # # tweets_df4.to_csv(filname4 ,index=False)
        #
        # df = pd.read_csv(filname2)
        # d = dtale.show(df)
        # d.open_browser()
        # result_c_s = "successfully completed with {} results".format(len(twts))
        # print(result_c_s)
        #
        # return render(request, 'index5.html', {"result_c_s": result_c_s})


    # os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} until:{} lang:{}"> '
    #           'text-query-tweets2.json'.format(tweet_count, since_date, text_query, fromuser, until_date, lang))
    # tweets_df2 = pd.read_json('text-query-tweets2.json', lines=True)
    # result3 = "successfully completed with {} results".format(len(tweets_df2))
    # return render(request, 'index5.html', {"result3": result3})


#----------------------------- end of complex snscraper  ----------------------------




def components(request):
    return render(request,'components.html',{})

def home_view(request):
    return render(request,'main.html',{})


def index(request):
    return render(request,'index.html',{})


def index2(request):
    return render(request,'index2.html',{})


def index3(request):
    return render(request,'index3.html',{})

def index4(request):
    return render(request,'index4.html',{})

def index5(request):
    return render(request,'index5.html',{})

def brows(request):
    return render(request,'brows.html',{})

def footer(request):
    return render(request,'footer.html',{})

def navbar(request):
    return render(request,'navbar.html',{})

def header(request):
    return render(request,'header.html',{})


def signin(request):
    return render(request,'signin.html',{})


def signup(request):
    return render(request,'signup.html',{})

def sidebarleft(request):
    return render(request,'sidebar-left.html',{})

def sidebarright(request):
    return render(request,'sidebar-right.html',{})
def contact(request):
    return render(request,'contact.html',{})
def about(request):
    return render(request,'about.html',{})
def portfoliodetails(request):
    return render(request,'portfolio-details.html',{})
def googlesearch(request):
    return render(request,'googlesearch.html',{})



mydates = []
def datecreator(t1,t2,coday):
  t1=datetime.strptime(t1,'%d/%m/%Y').date()
  t2=datetime.strptime(t2,'%d/%m/%Y').date()
  k=int((t2-t1).days)
  print(k)
  print(t1)
  print(type(t1))
  t = timedelta(days = int(coday))
  dates = np.arange(t1, t2, t).astype(datetime)
  for date in dates:
    newdate=date.strftime('%m/%d/%Y')
    mydates.append(newdate)
  return mydates


####################################### tweepy query  ##############################

def search_tweepy_query(request):
    query_key = request.GET.get("query_key")
    query_secret = request.GET.get("query_secret")
    query_atoken = request.GET.get("query_atoken")
    query_asecret = request.GET.get("query_asecret")
    query_search = request.GET.get("query_search")
    query_maxresult = request.GET.get("query_maxresult")
    query_lang = request.GET.get("query_lang")
    query_filname = request.GET.get("query_filname")
    query_filname=query_filname+'.csv'
    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h = os.getcwd()
    query_filname2 = query_filname
    # header = ["user_id", "user_name", "text", "tweet_id", "created_at", "language"]
    if (h.startswith("/home")):
        try:
            fa = str(query_filname)
            query_filname = desktop + "/" + fa
            auth = tw.OAuthHandler(query_key, query_secret)
            auth.set_access_token(query_atoken, query_asecret)
            api = tw.API(auth, wait_on_rate_limit=True)
            tweets = api.search_tweets(q=query_search, lang=query_lang, count=query_maxresult)

            d = pd.DataFrame(tweets['statuses'])
            y = pd.json_normalize(d.user)
            y.to_csv(query_filname, index=False)
            df_q = pd.read_csv(query_filname)
            ddf_q = dtale.show(df_q)
            ddf_q.open_browser()
            result_query = "successfully completed with {} results".format(len(y))
            print(result_query)
            return render(request, 'index5.html', {"result_query": result_query})

        except:
            pass
    else:
        print("----------------------except blogğuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu-------")
        desktop2 = desktop.replace("Desktop", "Masaüstü")
        fa2 = str(query_filname2)
        query_filname2 = desktop2 + "//" + fa2
        auth = tw.OAuthHandler(query_key, query_secret)
        auth.set_access_token(query_atoken, query_asecret)
        api = tw.API(auth, wait_on_rate_limit=True)
        tweets = api.search_tweets(q=query_search, lang=query_lang, count=query_maxresult)
        d2a = pd.DataFrame(tweets['statuses'])
        y2a = pd.json_normalize(d2a.user)
        y2a.to_csv(query_filname2, index=False)
        df2a = pd.read_csv(query_filname2)
        ddf2a = dtale.show(df2a)
        ddf2a.open_browser()
        result_query = "successfully completed with {} results".format(len(y2a))
        print(result_query)
        return render(request, 'index5.html', {"result_query": result_query})

#---------------------------------- end of tweepy query ---------------------------


####################################### tweepy timeline  ##############################

def search_tweepy_timeline(request):
    timeline_key = request.GET.get("timeline_key")
    timeline_secret = request.GET.get("timeline_secret")
    timeline_atoken = request.GET.get("timeline_atoken")
    timeline_asecret = request.GET.get("timeline_asecret")
    timeline_maxresult = request.GET.get("timeline_maxresult")
    timeline_filname = request.GET.get("timeline_filname")
    fl = str(timeline_filname)
    timeline_filname = fl + ".csv"

    auth = tw.OAuthHandler(timeline_key, timeline_secret)
    auth.set_access_token(timeline_atoken, timeline_asecret)

    api = tw.API(auth, wait_on_rate_limit=True, parser=tw.parsers.JSONParser())
    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h = os.getcwd()
    timeline_filname2 = timeline_filname
    header = ["user_id", "user_name", "text", "tweet_id", "created_at", "language"]
    if (h.startswith("/home")):
        try:
            fb = str(timeline_filname)
            timeline_filname = desktop + "/" + fb

            d2 = list(tw.Cursor(api.home_timeline).items(timeline_maxresult))
            d3 = pd.DataFrame(d2)
            y2 = pd.json_normalize(d3.user)
            print(y2)
            y2.to_csv(timeline_filname, index=False)
            df_2 = pd.read_csv(timeline_filname)
            d2_df = dtale.show(df_2)
            d2_df.open_browser()
            result_timeline = "successfully completed with {} results".format(len(y2))
            print(result_timeline)
            return render(request, 'index5.html', {"result_timeline": result_timeline})



        except:
            pass
    else:
        try:
            fb2 = str(timeline_filname2)
            timeline_filname2 = desktop + "//" + fb2

            d2b = list(tw.Cursor(api.home_timeline).items(timeline_maxresult))
            d3b = pd.DataFrame(d2b)
            y2b = pd.json_normalize(d3b.user)
            y2b.to_csv(timeline_filname2, index=False)
            df_22b = pd.read_csv(timeline_filname2)
            d22_dfb = dtale.show(df_22b)
            d22_dfb.open_browser()
            result_timeline = "successfully completed with {} results".format(len(y2b))
            print(result_timeline)
            return render(request, 'index5.html', {"result_timeline": result_timeline})


        except:
            pass

#---------------------------------- end of tweepy timeline ---------------------------


####################################### tweepy geo  ##############################
# self, key, secret, atoken, asecret, max_result_3, filname_3):
def search_tweepy_geo(request):
    geo_key = request.GET.get("geo_key")
    geo_secret = request.GET.get("geo_secret")
    geo_atoken = request.GET.get("geo_atoken")
    geo_asecret = request.GET.get("geo_asecret")
    geo_code = request.GET.get("geo_code")
    geo_filname = request.GET.get("geo_filname")
    fl = str(geo_filname)
    geo_filname = fl + ".csv"

    auth = tw.OAuthHandler(geo_key, geo_secret)
    auth.set_access_token(geo_atoken, geo_asecret)
    # api = tw.API(auth, wait_on_rate_limit=True)
    api = tw.API(auth, wait_on_rate_limit=True, parser=tw.parsers.JSONParser())

    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h = os.getcwd()
    geo_filname2 = geo_filname
    header = ["user_id", "user_name", "text", "tweet_id", "created_at", "language"]
    if (h.startswith("/home")):
        try:
            ff = str(geo_filname)
            geo_filname = desktop + "/" + ff
            print(geo_filname)


            top_trends = api.get_place_trends(geo_code)
            d_3_ = pd.json_normalize(top_trends[0]['trends'])
            print("tooooooooooo csv 3333333")

            # d_3 = list(tw.Cursor(api.home_timeline).items(self.max_result_3))
            # d_3_ = pd.DataFrame(d_3)
            # y3 = pd.json_normalize(d_3_.user)
            d_3_.to_csv(geo_filname, index=False)
            df_3 = pd.read_csv(geo_filname)
            d3_df = dtale.show(df_3)
            d3_df.open_browser()
            result_geo = "successfully completed with {} results".format(len(d_3_))
            print(result_geo)
            return render(request, 'index5.html', {"result_geo": result_geo})



        except:
            pass
    else:
        try:
            ff2 = str(geo_filname2)
            geo_filname2= desktop + "//" + ff2
            print("aaaaaaaaaaaa")

            print("???????????????????????????")

            print(geo_filname2)

            top_trends = api.get_place_trends(geo_code)
            d_3_2 = pd.json_normalize(top_trends[0]['trends'])
            print("tooooooooooo csv 3333333")
            # d_3 = list(tw.Cursor(api.home_timeline).items(self.max_result_3))
            # d_3_ = pd.DataFrame(d_3)
            # y3 = pd.json_normalize(d_3_.user)
            d_3_2.to_csv(geo_filname2, index=False)
            df_32 = pd.read_csv(geo_filname2)
            d3_df2 = dtale.show(df_32)
            d3_df2.open_browser()
            result_geo = "successfully completed with {} results".format(len(d_3_2))
            print(result_geo)
            return render(request, 'index5.html', {"result_geo": result_geo})


        except:
            pass
#---------------------------------- end of tweepy geo ---------------------------




#
# ################################## complex snscrape #################################
#
# def complex_snscrape(request):
#     tweet_count = request.GET.get("tweet_count")
#     since_date = request.GET.get("since_date")
#     text_query = request.GET.get("text_query")
#     fromuser = request.GET.get("fromuser")
#     lang = request.GET.get("lang")
#     filname = request.GET.get("filname")
#     fl=str(filname)
#     filname = fl + ".csv"
#     # result_c_s="bos"
#
#
#     try:
#         desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
#         print(desktop)
#     except:
#         print("Linux Veya Unix Yolu Bulunamadı")
#     h = os.getcwd()
#     filname2 = filname
#     if (h.startswith("/home")):
#         try:
#             ff = str(filname)
#             filname = desktop + "/" + filname
#             os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} lang:{}"> {}'
#                       .format(tweet_count, since_date, text_query, fromuser, lang, filname))
#             filname8 = str(filname)
#             download_file(filname8)
#             # raw_tweets = pd.read_json(filname8, lines=True)
#             # raw_tweets.to_csv(filname8,index=None)
#             df = pd.read_csv(filname8)
#             d = dtale.show(df)
#             d.open_browser()
#             result_c_s = "successfully completed with"# {} results".format(len(raw_tweets))
#             print(result_c_s)
#             return render(request, 'index5.html', {"result_c_s": result_c_s})
#
#
#         except:
#             print("pathway problem occurred for complex search . Please check your pathway")
#             pass
#     else:
#         desktop2 = desktop.replace("Desktop", "Masaüstü")
#         ff = str(filname2)
#         filname2 = desktop2 + "//" + filname2
#         os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} lang:{}"> {}'
#                   .format(tweet_count, since_date, text_query, fromuser, lang, filname))
#
#         raw_tweets = pd.read_json(filname2, lines=True)
#         # result3 = "successfully completed with {} results".format(len(raw_tweets))
#         users = json_normalize(raw_tweets['user'])
#         users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
#         users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
#         # Create DataFrame and remove duplicates
#         users = pd.DataFrame(users)
#         # users.drop_duplicates(subset=['userId'], inplace=True)
#         # Transform 'raw_tweets' DataFrame
#         # Add column for 'userId'
#         user_id = [user['id'] for user in raw_tweets['user']]
#         raw_tweets['userId'] = user_id
#         # Remove less important columns
#         cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
#                 'quoteCount']
#         tweets = raw_tweets[cols]
#         tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
#         cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
#                 'location']
#         use = users[cols]
#         twts = use.merge(tweets, on='userId')
#         twts.to_csv(filname2, index=False)
#         # tweets_df4.to_csv(filname4 ,index=False)
#
#         df = pd.read_csv(filname2)
#         d = dtale.show(df)
#         d.open_browser()
#         result_c_s = "successfully completed with {} results".format(len(twts))
#         print(result_c_s)
#
#         return render(request, 'index5.html', {"result_c_s": result_c_s})
#
#
#     # os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} until:{} lang:{}"> '
#     #           'text-query-tweets2.json'.format(tweet_count, since_date, text_query, fromuser, until_date, lang))
#     # tweets_df2 = pd.read_json('text-query-tweets2.json', lines=True)
#     # result3 = "successfully completed with {} results".format(len(tweets_df2))
#     # return render(request, 'index5.html', {"result3": result3})
#
#
# #----------------------------- end of complex snscraper  ----------------------------

####################################### simple snscrape ##############################

def simple_snscrape(request):
    tweet_count2 = request.GET.get("tweet_count2")
    since_date2 = request.GET.get("since_date2")
    text_query2 = request.GET.get("text_query2")
    filname4 = request.GET.get("filname4")
    fn=str(filname4)
    filname4 = fn + ".csv"
    mm2=filname4
    # result_s_s="bos"


    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h = os.getcwd()
    filname5 = filname4
    if (h.startswith("/home")):

        try:
            ff = str(filname4)
            # filname4 = desktop + "/" + ff
            filname4 = desktop[:-7] + "websites/rubic/webapp/upload/" + ff

            print("------------------")
            print(filname4)
            print("------------------")
            os.system(
                "snscrape --jsonl --progress --max-results {} --since {} twitter-search '{}'> {}".format(
                    tweet_count2, since_date2, text_query2, filname4))
            filname8 = str(mm2)

            raw_tweets = pd.read_json(filname4, lines=True)
            raw_tweets.to_csv(filname4, index=False)

            print("----------------------------------")
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filepath = BASE_DIR + '/upload/' + filname8
            print(filepath)
            # Open the file for reading content
            path = open(filepath, 'rb')
            # Set the mime type
            mime_type, _ = mimetypes.guess_type(filepath)
            # Set the return value of the HttpResponse
            response = HttpResponse(path, content_type=mime_type)
            # Set the HTTP header for sending to browser
            response['Content-Disposition'] = "attachment; filename=%s" % filname8
            h = dtale.show()
            h.main_url()
            return response
            # filname44 = str(filname4)
            # raw_tweets = pd.read_json(filname44, lines=True, encoding='utf-8')
            # raw_tweets.to_csv(filname44, index=None)
            # df = pd.read_csv(filname44)
            # d = dtale.show(df)
            # d.open_browser()
            result_s_s = "successfully completed with "#{} results".format(len(raw_tweets))
            # result_s_s = "successfully completed with {} results"
            print(result_s_s)
            return render(request, 'index5.html', {"result_s_s": result_s_s})


    # return render(request, 'index5.html', {"result_s_s": result_s_s})


        except:
            print("pathway problem occurred for simple search. Please check your pathway")
            pass
    else:
        pass
    #     desktop2 = desktop.replace("Desktop", "Masaüstü")
    #     ff = str(filname5)
    #     filname5 = desktop2 + "//" + filname5
    #     os.system(
    #         "snscrape --jsonl --progress --max-results {} --since {} twitter-search '{}'> {}".format(
    #             tweet_count2, since_date2, text_query2, filname5))
    #     # tweets_df5 = pd.read_json(filname5, lines=True,encoding='utf-8')
    #
    #     raw_tweets = pd.read_json(filname5, lines=True, encoding='utf-8')
    #     # raw_tweets=tweet
    #     users = json_normalize(raw_tweets['user'])
    #     users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
    #     users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
    #     # Create DataFrame and remove duplicates
    #     users = pd.DataFrame(users)
    #     # users.drop_duplicates(subset=['userId'], inplace=True)
    #     # Transform 'raw_tweets' DataFrame
    #     # Add column for 'userId'
    #     user_id = [user['id'] for user in raw_tweets['user']]
    #     raw_tweets['userId'] = user_id
    #     # Remove less important columns
    #     cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
    #             'quoteCount']
    #     tweets = raw_tweets[cols]
    #     tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
    #     cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
    #             'location']
    #     use = users[cols]
    #     twts = use.merge(tweets, on='userId')
    #     twts.to_csv(filname5, index=False)
    #     df = pd.read_csv(filname5)
    #     d = dtale.show(df)
    #     d.open_browser()
    #
    #     # tweets_df5.to_csv(filname5 ,index=False)
    #     result_s_s = "successfully completed with {} results".format(len(twts))
    #     print(result_s_s)
    #     return render(request, 'index5.html', {"result_s_s": result_s_s})

#---------------------------------- end of simple snscrape ---------------------------


##################################### facebook #########################################

def handle_pagination_url(url,ccid):
    global start_url
    start_url = url
    resq = []
    while True:
        try:
            post = next(
                get_posts(
                    post_urls=ccid,
                    options={
                        "comments": "generator",
                        "comment_start_url": start_url,
                        "comment_request_url_callback": handle_pagination_url,
                    },
                )
            )
            comments = post["comments_full"]
            for comment in comments:
                print(comment)
                resq.append(comment)
            print("All done")
            break
        except exceptions.TemporarilyBanned:
            print("Temporarily banned, sleeping for 10m")
            time.sleep(600)
    return resq




def faceb(request):
    fbkey = request.GET.get("fbkey")
    fname=request.GET.get("fname")
    posts=[]
    count=0
    enable_logging(logging.DEBUG)
    a_logger = logging.getLogger()
    start = time.time()
    res=[]
    print(fbkey)
    print("befffffffffffor ")

    if fbkey != None:

        print("in ifffffffffffffff")
        try:
            for post in get_posts(fbkey, cookies="/home/bilgi/cookies.txt", pages=200, timeout=60,
                                  options={"comments": True, "allow_extra_requests": False, "posts_per_page": 200}):
                count+=1
                posts.append(post)
                df=post['post_url']
                df2 = post['post_id']
                print("rrrrrrrrrrrrrrrrrrrrrrrrr")
                # hh=handle_pagination_url(df,df2)
                print("ssssssssssssssssssssssssssss")
                # print(hh)





        except:
            print(
                f"{len(posts)} posts retrieved in {round(time.time() - start)}s. Oldest post: {posts[-1].get('time')}")

        df1 = pd.DataFrame(posts)
        print(df1)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/upload/' + fname+'.csv'
        df1.to_csv(filepath, index=False, header=True)

        print("----------------------------------")

        # filepath = BASE_DIR + '/upload/' + fname
        print(filepath)
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % fname+'.csv'
        h = dtale.show()
        h.main_url()
        return response
        # filname44 = str(filname4)
        # raw_tweets = pd.read_json(filname44, lines=True, encoding='utf-8')
        # raw_tweets.to_csv(filname44, index=None)
        # df = pd.read_csv(filname44)
        # d = dtale.show(df)
        # d.open_browser()
        result_s_s = "successfully completed with "  # {} results".format(len(raw_tweets))
        # result_s_s = "successfully completed with {} results"
        print(result_s_s)
        return render(request, 'index5.html', {"result_s_s": result_s_s})



        fbresult = "Facebook search completed with {} results successfully ".format(count)
    else:
        pass
    return render(request, 'index5.html', {"fbresult": fbresult})




#------------------------------end of facebook ------------------------------------------------

##################################### reddit #########################################
# secret=	C0QWuVft5b2jj4Dt61fnxYQJ2merHA
# zlBNt1g_Ht7bsNojj3HPUQ

# secret = 	Lne3wZiWiJz9JkYefC5oSwxItl4hlQ
#  yjm7M5bmS3lxlrT_rPmTxQ
def search_reddit(request):
    reddit_keyword = request.GET.get("rdkey")
    fname = request.GET.get("fname")
    my_client_id=request.GET.get("reddit_client_id")
    my_client_secret=request.GET.get("reddit_client_secret")
    my_user_agent=request.GET.get("reddit_user_agent")

    reddit = praw.Reddit(client_id='my_client_id',
                         client_secret='my_client_secret',
                         user_agent='my_user_agent')

    hot_posts = reddit.subreddit(reddit_keyword).hot(limit=10)



    pass

#------------------------------end of reddit ------------------------------------------------

################################################################### part 2 #############################################

####################################### google all search   ############################
def add(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    fname = request.GET.get("fname")
    date1 = request.GET.get("date1")
    date1=datetime.strptime(date1,'%Y-%m-%d').date()
    date1=date1.strftime('%d/%m/%Y')
    date2 = request.GET.get("date2")
    date2=datetime.strptime(date2,'%Y-%m-%d').date()
    date2=date2.strftime('%d/%m/%Y')
    # fname=fname+'.csv'

    vord_add = num1.split(',')
    links_add = num2.split(',')
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    print(desktop)
    way = "{}{}{}/".format(desktop[:-7], "websites/rubic/webapp/g_upload/", fname)
    print(way)
    try:
        os.makedirs(way, exist_ok=True)
        print("Directory '%s' created successfully" % fname)
    except OSError as error:
        newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname
    file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)

    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        fnames = file_path+ "/" + fname + '.csv'
        fnames2=file_path+ "/" + fname + '_content.csv'
        print(desktop)

    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h = os.getcwd()
    fname2 = fnames
    ######################### for linux
    if (h.startswith("/home")):
        for vord in vord_add:
            non = 0
            vord = vord.strip()

            for plink in links_add:
                plink = plink.strip()

                google = google_search(vord, plink, fnames, date1, date2)
                try:
                    for i in google.urls:
                        non += 1
                except AttributeError:
                    pass
        file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
        print(file_path)
        zf = "{}/{}".format(file_path, fname)
        print(zf)
        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
        # url='/home/bilgi/websites/rubic/webapp/g_upload/Ahmetcvddv/Ahmetcvddv.csv'
        with open(fnames) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                try:
                    if line_count == 0:
                        # print(row.text)
                        print(row)
                        print("baslangıç 0 noktası")
                        print("======")
                        line_count += 1
                        pass
                    else:
                        # print("1 noktası")
                        # r = requests.get(row)
                        # print("1111 noktası")
                        # if r.status_code != 200 or r.status_code == 503 or r.status_code == 404 or r.status_code == 405:
                        #     continue
                        # if line_count==0:
                        #     # print(row.text)
                        #     print(row)
                        #     print("======")
                        #     pass
                        # else:
                        print(row)
                        print("======")
                        print("burdayım")
                        surl=f'{", ".join(row)}'
                        surl2=str(surl)
                        # print(surl)
                        article = NewsPlease.from_url(surl2.strip())
                        fieldnames = ['url', 'date', 'title', 'content']
                        a=article.url
                        try:
                            b=article.date_publish
                        except:
                            b="None"
                        try:
                            c=article.title
                        except:
                            c="None"
                        try:
                            d = article.maintext
                            dd = " ".join(d.split())
                        except:
                            dd = "None"
                        sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                        # rows = [
                        #     {'url': '{}'.format(a),
                        #      'date':'{}'.format(b),
                        #      'title': '{}'.format(c),
                        #      'content': '{}'.format(d)}]


                        # with open(fnames2, 'a') as file:
                        #     file.write(sent_line + '\n')
                        with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                            csvwriter = csv.writer(csvfile, delimiter=' ')
                            csvwriter.writerow([sent_line])
                        #     for lin in linky:
                        #         csvwriter.writerow([lin])
                        #         print("sssssssss")
                        print("close csv")

                        #########################################333333
                        # counter=0

                        # with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                        #     print("open csv")
                        #     csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        #     # if counter==0:
                        #     #     csvwriter.writerow(rows)
                        #     # for lin in linky:
                        #     csvwriter.writerow(fieldnames)
                        #     csvwriter.writerow(rows)

                        # with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
                        #     writer = csv.DictWriter(f, fieldnames=fieldnames)
                        #     writer.writeheader()
                        #     writer.writerows(rows)

                        line_count += 1

                except(
                        requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,
                        requests.exceptions.InvalidURL,
                        requests.exceptions.InvalidSchema, requests.exceptions.ConnectTimeout,
                        requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout,
                        requests.exceptions.BaseHTTPError):
                    continue

            print(f'Processed {line_count} lines.')

        shutil.make_archive(zf, 'zip', file_path,'{}_content.csv'.format(fname))
        zf_s = "{}{}".format(zf, '.zip')
        print(zf_s)

        file = open(zf_s, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)
        return response

        # result = "Your search on google by website finished successfully with {} links".format(non)
        # df2 = pd.read_csv(fname)
        # ddf2 = dtale.show(df2)
        #
        # ddf2.open_browser()
        #
        # return render(request, 'index.html', {"result": result})
    ##################   for   windows
    else:
        pass
        # for vord in vord_add:
        #     non = 0
        #     vord = vord.strip()
        #
        #     for plink in links_add:
        #         plink = plink.strip()
        #
        #         google = google_search8(vord, plink, fname, date1, date2)
        #         try:
        #             for i in google.urls:
        #                 non += 1
        #         except AttributeError:
        #             pass
        #
        # result = "Your search on google by website finished successfully with {} links".format(non)
        # df2 = pd.read_csv(fname)
        # ddf2 = dtale.show(df2)
        #
        # ddf2.open_browser()
        #
        # return render(request, 'index.html', {"result": result})

#####---------------------------  end of    google all search    ---------------------------------




##########################      google detail search      ######################

def add_google_detail(request):
    num1_det = request.GET.get("num1_det")
    num2_det = request.GET.get("num2_det")
    aralik_det=request.GET.get("aralik_det")
    fname_det = request.GET.get("fname_det")

    date1_det = request.GET.get("date1_det")
    date1_det = datetime.strptime(date1_det, '%Y-%m-%d').date()
    date1_det = date1_det.strftime('%d/%m/%Y')

    date2_det = request.GET.get("date2_det")
    date2_det = datetime.strptime(date2_det, '%Y-%m-%d').date()
    date2_det = date2_det.strftime('%d/%m/%Y')

    mydates2=datecreator(date1_det,date2_det,aralik_det)
    fname=fname_det

    h=num1_det.split(',')
    z=num2_det.split(',')

    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    print(desktop)
    way = "{}{}{}/".format(desktop[:-7], "websites/rubic/webapp/g_upload/", fname)
    print(way)
    try:
        os.makedirs(way, exist_ok=True)
        print("Directory '%s' created successfully" % fname)
    except OSError as error:
        newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname
    file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
    # fnames2 = file_path + "/" + fname + '_content.csv'

    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        fnames = file_path + "/" + fname + '.csv'
        fnames2 = file_path + "/" + fname + '_content.csv'
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    hos = os.getcwd()
    fname_det2=fname_det
    ######################### for linux
    if (hos.startswith("/home")):
        fname_det = file_path + "/" + fname_det + '.csv'
        for vord in h:
            vord = vord.strip()

            for plink in z:
                plink = plink.strip()

                for j in range(len(mydates2) - 1):
                    google = google_search7(vord, plink, fname_det, mydates2[j], mydates2[j + 1])
                    non = 0
                    print("***************** jjjjjjjjjjjjjjjjjjjjjjj ")
                    print(j)
                    print("***************** jjjjjjjjjjjjjjjjjjjjjjj ")
                    try:
                        for i in google.urls:
                            non += 1
                    except AttributeError:
                        break
                        # j=int(len(mydates2)-2)
                        # pass
        file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
        print(file_path)
        zf = "{}/{}".format(file_path, fname)
        print(zf)
        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")

        with open(fnames) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                try:
                    if line_count == 0:
                        # print(row.text)
                        print(row)
                        print("baslangıç 0 noktası")
                        print("======")
                        line_count += 1
                        pass
                    else:
                        # print("1 noktası")
                        # r = requests.get(row)
                        # print("1111 noktası")
                        # if r.status_code != 200 or r.status_code == 503 or r.status_code == 404 or r.status_code == 405:
                        #     continue
                        # if line_count==0:
                        #     # print(row.text)
                        #     print(row)
                        #     print("======")
                        #     pass
                        # else:
                        print(row)
                        print("======")
                        print("burdayım")
                        surl=f'{", ".join(row)}'
                        surl2=str(surl)
                        # print(surl)
                        article = NewsPlease.from_url(surl2.strip())
                        fieldnames = ['url', 'date', 'title', 'content']
                        a=article.url
                        try:
                            b=article.date_publish
                        except:
                            b="None"
                        try:
                            c=article.title
                        except:
                            c="None"
                        try:
                            d = article.maintext
                            dd = " ".join(d.split())
                        except:
                            dd = "None"
                        sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                        # rows = [
                        #     {'url': '{}'.format(a),
                        #      'date':'{}'.format(b),
                        #      'title': '{}'.format(c),
                        #      'content': '{}'.format(d)}]


                        # with open(fnames2, 'a') as file:
                        #     file.write(sent_line + '\n')
                        with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                            csvwriter = csv.writer(csvfile, delimiter=' ')
                            csvwriter.writerow([sent_line])
                        #     for lin in linky:
                        #         csvwriter.writerow([lin])
                        #         print("sssssssss")
                        print("close csv")

                        #########################################333333
                        # counter=0

                        # with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                        #     print("open csv")
                        #     csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        #     # if counter==0:
                        #     #     csvwriter.writerow(rows)
                        #     # for lin in linky:
                        #     csvwriter.writerow(fieldnames)
                        #     csvwriter.writerow(rows)

                        # with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
                        #     writer = csv.DictWriter(f, fieldnames=fieldnames)
                        #     writer.writeheader()
                        #     writer.writerows(rows)

                        line_count += 1

                except(
                        requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,
                        requests.exceptions.InvalidURL,
                        requests.exceptions.InvalidSchema, requests.exceptions.ConnectTimeout,
                        requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout,
                        requests.exceptions.BaseHTTPError):
                    continue

            print(f'Processed {line_count} lines.')








        shutil.make_archive(zf, 'zip', file_path,'{}_content.csv'.format(fname))#,'{}.zip'.format(fname))
        zf_s = "{}{}".format(zf, '.zip')
        print(zf_s)

        file = open(zf_s, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)
        return response
        # google_detail_result = "Your search on google by website finished successfully with {} links".format(non)
        # df2 = pd.read_csv(fname_det)
        # ddf2 = dtale.show(df2)
        #
        # ddf2.open_browser()
        #
        # return render(request, 'index5.html', {"google_detail_result": google_detail_result})
        #

        ##########################    for windows
    else:
        pass
        # fname_det2 = desktop + "//" + fname_det2 + '.csv'
        # for vord in h:
        #     vord = vord.strip()
        #
        #     for plink in z:
        #         plink = plink.strip()
        #
        #         for j in range(len(mydates2) - 1):
        #             google = google_search7(vord, plink, fname_det, mydates2[j], mydates2[j + 1])
        #             non = 0
        #             try:
        #                 for i in google.urls:
        #                     non += 1
        #             except AttributeError:
        #                 pass
        # google_detail_result = "Your search on google by website finished successfully with {} links".format(non)
        # df2 = pd.read_csv(fname_det)
        # ddf2 = dtale.show(df2)
        #
        # ddf2.open_browser()
        #
        # return render(request, 'index.html', {"google_detail_result": google_detail_result})

###--------------------------end  of ----------------- google detail search      -------------##



##################################       google topic  ###################################

def topic_google_add(request):
    btnum1 = request.GET.get("btnum1")
    btnum2 = request.GET.get("btnum2")
    btfname = request.GET.get("btfname")
    btdate1 = request.GET.get("btdate1")
    btdate1 = datetime.strptime(btdate1, '%Y-%m-%d').date()
    btdate1 = btdate1.strftime('%d/%m/%Y')
    btdate2 = request.GET.get("btdate2")
    btdate2 = datetime.strptime(btdate2, '%Y-%m-%d').date()
    btdate2 = btdate2.strftime('%d/%m/%Y')
    fname=btfname

    vord_bing = btnum1.split(',')
    links_bing = btnum2.split(',')
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    print(desktop)
    way = "{}{}{}/".format(desktop[:-7], "websites/rubic/webapp/g_upload/", fname)
    print(way)
    try:
        os.makedirs(way, exist_ok=True)
        print("Directory '%s' created successfully" % fname)
    except OSError as error:
        newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname
    file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)

    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        fnames = file_path + "/" + fname + '.csv'
        fnames2 = file_path + "/" + fname + '_content.csv'
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h_bing = os.getcwd()
    btffname2 = btfname
    ######################### for linux
    if (h_bing.startswith("/home")):
        noc = 0
        btfname = file_path + "/" + btfname + '.csv'
        print("=================--------------============")
        print(btfname)
        for vord_bing in vord_bing:

            vord_bing = vord_bing.strip()

            for plink_bing in links_bing:
                plink_bing = plink_bing.strip()

                googletb = google_search6(vord_bing, plink_bing, btfname, btdate1, btdate2)

                try:
                    for i in googletb.urls:
                        noc += 1
                except AttributeError:
                    pass
        topic_result = "Your search on google by topic finished successfully with {} links".format(noc)
        file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
        print(file_path)
        zf = "{}/{}".format(file_path, fname)
        print(zf)
        print(fnames)
        print(fnames2)
        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")

        with open(fnames) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                try:
                    if line_count == 0:
                        # print(row.text)
                        print(row)
                        print("baslangıç 0 noktası")
                        print("======")
                        line_count += 1
                        pass
                    else:
                        # print("1 noktası")
                        # r = requests.get(row)
                        # print("1111 noktası")
                        # if r.status_code != 200 or r.status_code == 503 or r.status_code == 404 or r.status_code == 405:
                        #     continue
                        # if line_count==0:
                        #     # print(row.text)
                        #     print(row)
                        #     print("======")
                        #     pass
                        # else:
                        print(row)
                        print("======")
                        print("burdayım")
                        surl = f'{", ".join(row)}'
                        surl2 = str(surl)
                        # print(surl)
                        article = NewsPlease.from_url(surl2.strip())
                        # fieldnames = ['url', 'date', 'title', 'content']
                        a = article.url
                        try:
                            b = article.date_publish
                        except:
                            b = "None"
                        try:
                            c = article.title
                        except:
                            c = "None"
                        try:
                            d = article.maintext
                            dd = " ".join(d.split())
                        except:
                            dd = "None"
                        sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                        # rows = [
                        #     {'url': '{}'.format(a),
                        #      'date':'{}'.format(b),
                        #      'title': '{}'.format(c),
                        #      'content': '{}'.format(d)}]

                        # with open(fnames2, 'a') as file:
                        #     file.write(sent_line + '\n')
                        with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                            csvwriter = csv.writer(csvfile, delimiter=' ')
                            csvwriter.writerow([sent_line])
                        #     for lin in linky:
                        #         csvwriter.writerow([lin])
                        #         print("sssssssss")
                        print("close csv")

                        #########################################333333
                        # counter=0

                        # with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                        #     print("open csv")
                        #     csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        #     # if counter==0:
                        #     #     csvwriter.writerow(rows)
                        #     # for lin in linky:
                        #     csvwriter.writerow(fieldnames)
                        #     csvwriter.writerow(rows)

                        # with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
                        #     writer = csv.DictWriter(f, fieldnames=fieldnames)
                        #     writer.writeheader()
                        #     writer.writerows(rows)

                        line_count += 1

                except(
                        requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,
                        requests.exceptions.InvalidURL,
                        requests.exceptions.InvalidSchema, requests.exceptions.ConnectTimeout,
                        requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout,
                        requests.exceptions.BaseHTTPError):
                    continue

            print(f'Processed {line_count} lines.')

        shutil.make_archive(zf, 'zip', file_path,'{}_content.csv'.format(fname))#,'{}.zip'.format(fname))
        zf_s = "{}{}".format(zf, '.zip')
        print(zf_s)

        file = open(zf_s, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)
        return response
    # return render(request, 'index.html', {"topic_result": topic_result})
    ################ for window
    else:
        pass
    #     noc = 0
    #     btfname = desktop + "/" + btfname + '.csv'
    #     for vord_bing in vord_bing:
    #
    #         vord_bing = vord_bing.strip()
    #
    #         for plink_bing in links_bing:
    #             plink_bing = plink_bing.strip()
    #
    #             googletb = google_search6(vord_bing, plink_bing, btfname, btdate1, btdate2)
    #
    #             try:
    #                 for i in googletb.urls:
    #                     noc += 1
    #             except AttributeError:
    #                 pass
    #     topic_result = "Your search on google by topic finished successfully with {} links".format(noc)
    #
    # # df2 = pd.read_csv(fname_det)
    # # ddf2 = dtale.show(df2)
    # #
    # # ddf2.open_browser()
    # return render(request, 'index.html', {"topic_result": topic_result})



    #
    # if btnum1!=None and btnum2!=None:
    #     googletb=google_search6(btnum1, btnum2,btfname,btdate1,btdate2)
    #     # bingsearch3 = Bing3(btnum1, btnum2, btfname)
    #     # count=bingsearch3.crawl_all()
    #     # bresult = "Bing search completed successfully"
    #     noc=0
    #     for i in googletb.urls:
    #         noc+=1
    #     topic_result="Your search on google by topic finished successfully with {} links".format(noc)
    # else:
    #     pass
    # return render(request,'index.html',{"topic_result": topic_result})
##########-------------------------- end of  google topic  ------------------------------------------------


#############      bing      #############################################################################


def bing_add(request):
    bnum1 = request.GET.get("bnum1")
    bnum2 = request.GET.get("bnum2")
    fname = request.GET.get("bfname")
    # bdate1 = request.GET.get("bdate1")
    # bdate2 = request.GET.get("bdate2")
    bresult="None"

    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    print(desktop)
    way = "{}{}{}/".format(desktop[:-7], "websites/rubic/webapp/g_upload/", fname)
    print(way)
    try:
        os.makedirs(way, exist_ok=True)
        print("Directory '%s' created successfully" % fname)
    except OSError as error:
        newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname
    file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)

    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        fnames = file_path + "/" + fname + '.txt'
        fnames2 = file_path + "/" + fname + '_content.csv'
        print(desktop)

    except:
        print("Linux Veya Unix Yolu Bulunamadı")


    # file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
    # try:
    #     desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    #     fnames = file_path + "/" + fname + '.txt'
    #     fnames2 = file_path + "/" + fname + '_content.csv'
    #     print(desktop)
    # except:
    #     pass

    if bnum1!=None and bnum2!=None:
        bingsearch=Bing(bnum1, bnum2,fname)
        bingsearch.crawl_all()
        bing_result="Bing search completed successfully"
        # desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        # fnames = file_path + "/" + fname + '.csv'
        # fnames2 = file_path + "/" + fname + '_content.csv'
        # print(desktop)
        # way = "{}{}{}/".format(desktop[:-7], "websites/rubic/webapp/g_upload/", fname)
        # print(way)

        # file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)



        # try:
        #     os.makedirs(way, exist_ok=True)
        #     print("Directory '%s' created successfully" % fname)
        # except OSError as error:
        #     newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname

        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
        print(file_path)
        zf = "{}/{}".format(file_path, fname)
        print(zf)
        print(fnames)
        print(fnames2)
        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
        # print("ok")



        with open(fnames) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                try:
                    if line_count == 0:
                        # print(row.text)
                        print(row)
                        print("baslangıç 0 noktası")
                        print("======")
                        line_count += 1
                        pass
                    else:
                        # print("1 noktası")
                        # r = requests.get(row)
                        # print("1111 noktası")
                        # if r.status_code != 200 or r.status_code == 503 or r.status_code == 404 or r.status_code == 405:
                        #     continue
                        # if line_count==0:
                        #     # print(row.text)
                        #     print(row)
                        #     print("======")
                        #     pass
                        # else:
                        print(row)
                        print("======")
                        print("burdayım")
                        surl = f'{", ".join(row)}'
                        surl2 = str(surl)
                        # print(surl)
                        article = NewsPlease.from_url(surl2.strip())
                        # fieldnames = ['url', 'date', 'title', 'content']
                        a = article.url
                        try:
                            b = article.date_publish
                        except:
                            b = "None"
                        try:
                            c = article.title
                        except:
                            c = "None"
                        try:
                            d = article.maintext
                            dd=" ".join(d.split())
                        except:
                            dd = "None"
                        sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                        # rows = [
                        #     {'url': '{}'.format(a),
                        #      'date':'{}'.format(b),
                        #      'title': '{}'.format(c),
                        #      'content': '{}'.format(d)}]

                        # with open(fnames2, 'a') as file:
                        #     file.write(sent_line + '\n')
                        with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                            csvwriter = csv.writer(csvfile, delimiter=' ')
                            csvwriter.writerow([sent_line])
                        #     for lin in linky:
                        #         csvwriter.writerow([lin])
                        #         print("sssssssss")
                        print("close csv")

                        #########################################333333
                        # counter=0

                        # with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                        #     print("open csv")
                        #     csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        #     # if counter==0:
                        #     #     csvwriter.writerow(rows)
                        #     # for lin in linky:
                        #     csvwriter.writerow(fieldnames)
                        #     csvwriter.writerow(rows)

                        # with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
                        #     writer = csv.DictWriter(f, fieldnames=fieldnames)
                        #     writer.writeheader()
                        #     writer.writerows(rows)

                        line_count += 1

                except(
                        requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,
                        requests.exceptions.InvalidURL,
                        requests.exceptions.InvalidSchema, requests.exceptions.ConnectTimeout,
                        requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout,
                        requests.exceptions.BaseHTTPError):
                    continue

            print(f'Processed {line_count} lines.')









        shutil.make_archive(zf, 'zip', file_path,'{}_content.csv'.format(fname))#,'{}'.format(fname))#,'{}.zip'.format(fname))
        zf_s = "{}{}".format(zf, '.zip')
        print(zf_s)

        file = open(zf_s, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)
        return response

    else:
        pass
    # return render(request,'index5.html',{"bing_result":bing_result})
######------------ end of  -----------    bing   -----------------------------------------------------

########################## bing detail search #####################3

def bing_add_detail(request):
    bing_num1_det = request.GET.get("bing_num1_det")
    bing_num2_det = request.GET.get("bing_num2_det")
    # bing_date1_det = request.GET.get("bing_date1_det")
    # bing_date2_det = request.GET.get("bing_date2_det")
    # bing_aralik_det = request.GET.get("bing_aralik_det")
    bing_fname_det = request.GET.get("bing_fname_det")
    bing_detail_result="None"
    # bing_detail_dates = datecreator(bing_date1_det, bing_date2_det, bing_aralik_det)

    vord_bing_detail = bing_num1_det.split(',')
    links_bing_detail = bing_num2_det.split(',')

    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h_bing_det = os.getcwd()
    bing_fname2_det = bing_fname_det
    ######################### for linux
    if (h_bing_det.startswith("/home")):
        noc = 0
        bing_fname_det = desktop + "/" + bing_fname_det + '.csv'
        for vord_bing_det in vord_bing_detail:

            vord_bing_det = vord_bing_det.strip()

            for plink_bing_det in links_bing_detail:
                plink_bing_det = plink_bing_det.strip()
                noc+=1

                bingsearch = Bing(vord_bing_det, plink_bing_det, bing_fname_det)
                bingsearch.crawl_all()
                bing_detail_result = "Bing search {} completed successfully".format(noc)

        # df2 = pd.read_csv(bing_fname_det)
        # ddf2 = dtale.show(df2)
        # ddf2.open_browser()
        file_path = os.path.join(settings.DOWNLOAD_G_ROOT, bing_fname_det)
        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
        print(file_path)
        zf = "{}/{}".format(file_path, bing_fname_det)
        print(zf)
        print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")

        shutil.make_archive(zf, 'zip', file_path,bing_fname_det)#,'{}.csv'.format(bing_fname_det))#,'{}.zip'.format(bing_fname_det))
        zf_s = "{}{}".format(zf, '.zip')
        print(zf_s)

        file = open(zf_s, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(bing_fname_det)
        return response



    else:
        noc = 0
        bing_fname2_det = desktop + "/" + bing_fname2_det + '.csv'
        for vord_bing_det in vord_bing_detail:

            vord_bing_det = vord_bing_det.strip()

            for plink_bing_det in links_bing_detail:
                plink_bing_det = plink_bing_det.strip()

                bingsearch = Bing(vord_bing_det, plink_bing_det, bing_fname2_det)
                bingsearch.crawl_all()
        bing_detail_result = "Bing search completed successfully"
        df2 = pd.read_csv(bing_fname_det)
        ddf2 = dtale.show(df2)

        ddf2.open_browser()

    return render(request, 'index5.html', {"bing_detail_result": bing_detail_result})

#****************    end of   bing detail search    ***************************


################################ factiva #########################################################

def search_factiva(request):
    pass
#---------------------------- end of factiva ---------------------------------------------------


##################################### newspapers ###############################################
def zipFiles(files):
    outfile = StringIO()  # io.BytesIO() for python 3
    with zipfile.ZipFile(outfile, 'w') as zf:
        for n, f in enumerate(files):
            zf.writestr("{}".format(n), f.getvalue())
    return outfile.getvalue()

def download_fol(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))


def download_file(url):
    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

async def main(uur):
    url = uur
    downloader = DDownloader()
    await downloader.crawl(url)  # fetch all the links from /directory/
    await downloader.download_files()  # download all files to current directory



def newspaper_search(request):
    # qq=request.GET.get("newspaper_keyword")
    q = request.GET.get("newspaper_keyword")
    fname=request.GET.get("newspaper_filename") #use as directory
    cl_names=request.GET.get("newspaper_names")

    fn = []
    link_list = []
    content_list = []
    file_list=[]
    # fname="denemef"
    way = ""
    # q=qq.split(",")
    cl = cl_names.split(",")
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    print(desktop)
    way = "{}{}{}/".format(desktop[:-7], "websites/rubic/webapp/g_upload/", fname)
    print(way)

    try:
        os.makedirs(way, exist_ok=True)
        print("Directory '%s' created successfully" % fname)
    except OSError as error:
        newspaper_result="Directory '%s' can not be created. Allready exist please change name and try again" % fname
        return render(request,'index5.html',{"newspaper_result":newspaper_result})

    # os.makedirs(way)
    # print("Directory '% s' created" % fname)

    for i in cl:
        h_link = "{}{}_{}_link.txt".format(way, fname, i)
        h_content = "{}{}_{}_content.txt".format(way, fname, i)
        link_list.append(h_link)
        content_list.append(h_content)

        # down_link_name = link_list.split('/')[-1]
        # down_content_name=content_list.split('/')[-1]
        file_list.append(h_link)
        file_list.append(h_content)

        h = "{}".format(i.strip())
        print(h)
        print("--------hhhhhhh ---------------")
        fn.append(h)
    ss = []
    for i in range(len(cl)):
        print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
        print(i)
        # ii = '{}={}("{}","{}","{}")'.format(cl[i], cl[i], q[i],fn[i], fname)
        ii = '{}={}(q,"{}","{}")'.format(cl[i], cl[i], fn[i], fname)
        print(ii)
        print("zzzzzzzzzzzzzzzzzzzzzzzz")
        ss.append(ii)
    zeta = []
    sayac = 0
    for i in ss:
        print(i)
        print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")
        exec(i)
        d_link = "{}".format(link_list[sayac])
        print("---------------------------------- dlink---------")
        print(d_link)
        print("???????????????????????")
        # download_file_g(d_link)

        # zipped_file = zipFiles(d_link)

        # url = "{}{}".format('/home/bilgi/websites/rubic/webapp/g_upload/',i)
        # r = requests.get(url, allow_redirects=True)
        # open('i', 'wb').write(r.content)

        z = i.split("=")
        print(z)
        zet = "{}{}".format(z[0], ".main()")
        zeta.append(zet)
        print("zeeeeeeeeeeettttttttttt")
        print(zet)
        exec(zet)
        d_content = ("{}".format(content_list[sayac]))
        print(" ***************** d_content ****************")
        print(d_content)
        print(" ***************** d_content ****************")
        # zipped_file = zipFiles(d_content)
        # download_file_g(d_content)
        sayac += 1


    # fn = []
    # link_list=[]
    # content_list=[]
    # # fname="deneme"
    # way=""
    # cl = cl_names.split(",")
    # desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    # print(desktop)
    # way="{}{}{}/".format(desktop[:-7],"websites/rubic/webapp/g_upload/",fname)
    # print(way)
    #
    # os.makedirs(way)
    # print("Directory '% s' created" % fname)
    #
    # for i in cl:
    #     h_link = "{}{}_{}_link.txt".format(way,fname,i)
    #     h_content = "{}{}_{}_content.txt".format(way,fname,i)
    #     link_list.append(h_link)
    #     content_list.append(h_content)
    #     h = "{}".format(i.strip())
    #     print(h)
    #     print("--------hhhhhhh ---------------")
    #     fn.append(h)
    # ss = []
    # for i in range(len(cl)):
    #     print(i)
    #     ii = '{}={}(q,"{}")'.format(cl[i], cl[i], fn[i])
    #     print(ii)
    #     ss.append(ii)
    # zeta = []
    # sayac=0
    # for i in ss:
    #     print(i)
    #     exec(i)
    #     d_link="{}".format(link_list[sayac])
    #     print(d_link)
    #     print("???????????????????????")
    #     # download_file_g(d_link)
    #
    #     # zipped_file = zipFiles(d_link)
    #
    #
    #     # url = "{}{}".format('/home/bilgi/websites/rubic/webapp/g_upload/',i)
    #     # r = requests.get(url, allow_redirects=True)
    #     # open('i', 'wb').write(r.content)
    #
    #     z = i.split("=")
    #     print(z)
    #     zet = "{}{}".format(z[0], ".main()")
    #     zeta.append(zet)
    #     print("zeeeeeeeeeeettttttttttt")
    #     print(zet)
    #     exec(zet)
    #     d_content=("{}".format(content_list[sayac]))
    #     # zipped_file = zipFiles(d_content)
    #     # download_file_g(d_content)
    #     sayac+=1

        # url = "{}{}".format('/home/bilgi/websites/rubic/webapp/g_upload/', zet)
        # r = requests.get(url, allow_redirects=True)
        # open('zet', 'wb').write(r.content)
    # download_file(way)
    # wget.download(way)
    # download_fol(way,"myfold")
    #
    # req = requests.get(way)
    # # Split URL to get the file name
    # down_filename = way.split('/')[-1]
    # # Writing the file to the local file system
    # with open(down_filename, 'wb') as output_file:
    #     output_file.write(req.content)
    # print('Downloading Completed')

    newspaper_result="succesfully completed"
    # response = HttpResponse(content_type='application/zip')
    # zip_file = zipfile.ZipFile(response, 'w')
    # for file_name in file_list:
    #     zip_file.write(file_name)
    # response['Content-Disposition'] = 'attachment; filename={}'.format(fname)
    # return response

    file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
    print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
    print(file_path)
    zf="{}/{}".format(file_path,fname)
    print(zf)
    print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")

    shutil.make_archive(zf,'zip',file_path,'{}_{}_content.txt'.format(fname,cl[0]))#,'{}'.format(fname))
    zf_s="{}{}".format(zf,'.zip')
    print(zf_s)

    file = open(zf_s, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)
    return response

    # asyncio.run(main(file_path))
    # print("completed")
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
    #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    #         return response
    # raise Http404

    #
    # response = HttpResponse(way, content_type='application/octet-stream')
    # response['Content-Disposition'] = "attachment; filename=%s" % way
    # # response['Content-Disposition'] = 'attachment; ' filename=%s" % filename
    # return response
    # return render(request, 'index5.html', {"newspaper_result": newspaper_result})





#
#
# def newspaper_search(request):
#     q=request.GET.get("newspaper_keyword")
#     fname=request.GET.get("newspaper_filename")
#     cl_names=request.GET.get("newspaper_names")
#     fn = []
#     cl = cl_names.split(",")
#     for i in cl:
#         h = "{}_{}".format(fname, i.strip())
#         fn.append(h)
#     ss = []
#     for i in range(len(cl)):
#         print(i)
#         ii = '{}={}(q,"{}")'.format(cl[i], cl[i], fn[i])
#         print(ii)
#         ss.append(ii)
#     zeta = []
#     for i in ss:
#         print(i)
#         exec(i)
#         download_file_g(i)
#
#         # url = "{}{}".format('/home/bilgi/websites/rubic/webapp/g_upload/',i)
#         # r = requests.get(url, allow_redirects=True)
#         # open('i', 'wb').write(r.content)
#
#         z = i.split("=")
#         print(z)
#         zet = "{}{}".format(z[0], ".main()")
#         zeta.append(zet)
#         print("zeeeeeeeeeeettttttttttt")
#         print(zet)
#         exec(zet)
#         download_file_g(zet)
#
#         # url = "{}{}".format('/home/bilgi/websites/rubic/webapp/g_upload/', zet)
#         # r = requests.get(url, allow_redirects=True)
#         # open('zet', 'wb').write(r.content)
#
#     newspaper_result="succesfully completed"
#     return render(request, 'index5.html', {"newspaper_result": newspaper_result})
#

#--------------------------end of newspapers                            -------------------------#


######################################### newspaper date search all #################################



def newspaper_search_all(request):

    date1=request.GET.get("date_first")
    date2=request.GET.get("date_last")

    category=request.GET.get("newspaper_category")
    cl_names_all=request.GET.get("newspaper_names_all")
    fname = request.GET.get("filename_all")  # use as directory

    # fname = request.GET.get("newspaper_filename")  # use as directory
    # cl_names = request.GET.get("newspaper_names")

    fn = []
    link_list = []
    content_list = []
    file_list = []

    # cl = cl_names_all.split(",")
    cl = cl_names_all.split(",")
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    print(desktop)
    way = "{}{}{}/".format(desktop[:-7], "websites/rubic/webapp/g_upload/", fname)
    print(way)

    try:
        os.makedirs(way, exist_ok=True)
        print("Directory '%s' created successfully" % fname)
    except OSError as error:
        newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname

        # return newspaper_result

    for i in cl:
        h_link = "{}{}_{}_link.txt".format(way, fname, i)
        h_content = "{}{}_{}_content.txt".format(way, fname, i)
        link_list.append(h_link)
        content_list.append(h_content)

        file_list.append(h_link)
        file_list.append(h_content)

        h = "{}".format(i.strip())
        print(h)
        print("--------hhhhhhh ---------------")
        fn.append(h)
    ss = []
    print(type(date1))
    for i in range(len(cl)):
        print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
        print(i)

        ii = '{}={}("{}","{}","{}","{}","{}")'.format(cl[i], cl[i], date1, date2, category, fn[i], fname)
        print(ii)
        print("zzzzzzzzzzzzzzzzzzzzzzzz")
        ss.append(ii)
    zeta = []
    sayac = 0
    for i in ss:
        print(i)
        print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")
        exec(i)
        d_link = "{}".format(link_list[sayac])
        print("---------------------------------- dlink---------")
        print(d_link)
        print("???????????????????????")

        z = i.split("=")
        print(z)
        zet = "{}{}".format(z[0], ".main()")
        zeta.append(zet)
        print("zeeeeeeeeeeettttttttttt")
        print(zet)
        exec(zet)
        d_content = ("{}".format(content_list[sayac]))
        print(" ***************** d_content ****************")
        print(d_content)
        print(" ***************** d_content ****************")
        # zipped_file = zipFiles(d_content)
        # download_file_g(d_content)
        sayac += 1

    newspaper_result="succesfully completed try another search"
    print(newspaper_result)

    file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # file_path = BASE_DIR + '/g_upload/' + fname
    print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
    print(file_path)
    zf="{}/{}".format(file_path,fname)
    print(zf)
    print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
    # shutil.make_archive(zf, 'zip', file_path, '{}.csv'.format(fname))

    shutil.make_archive(zf,'zip',file_path,'{}_{}_content.txt'.format(fname,cl[0]))#,'{}'.format(fname))
    zf_s="{}{}".format(zf,'.zip')
    print(zf_s)

    file = open(zf_s, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)
    return response
    # return render(request, 'index5.html', {"newspaper_result": newspaper_result})

#------------------------------------- end of newspaper date search all --------------------



#########################################################   PART 3  ###################################################


#########################  collectin article ###################################
def collect_article(request):
    collect_data_from = request.GET.get("collect_data_from")
    collect_data_to = request.GET.get("collect_data_to")
    collect_index_from = request.GET.get("collect_index_from")
    collect_index_to = request.GET.get("collect_index_to")
    collect_result=""
    index_choose="{}:{}".format(collect_index_from.strip(),collect_index_to.strip())
    print(index_choose)
    print(type(index_choose))
    myarr=[]
    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    col_data = os.getcwd()
    if (col_data.startswith("/home")):
        noc = 0
        with open(collect_data_from) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if row == 0:
                    pass
                else:
                    myarr.append(row)
        print("Reading from file is completed ")

        with open(collect_data_to, 'w', encoding='UTF8', newline='') as csvfileh:
            csvwriterh = csv.writer(csvfileh, delimiter=';')  # , quotechar='|', quoting=csv.QUOTE_MINIMAL
            csvwriterh.writerow(['url', 'publish_date', 'category', 'language', 'headline', 'article'])
        count = 0
        urc = 0
        for i in myarr[int(collect_index_from):int(collect_index_to)]: #"{}:{}".format(collect_index_from,collect_index_to)
            for j in i:
                t1 = time.time()
                rr = requests.get(j)
                t2 = time.time()
                tt = t2 - t1

                if rr.status_code != 200 or rr.status_code == 503 or tt > 60:
                    print("50000000000003333333333333333")
                    time.sleep(3)
                    continue
                else:

                    try:
                        urc += 1
                        print("-------------")
                        print(urc)
                        print("-------------")
                        collect_article_result = "The last link is {} . if the crawl not finished yet use this number".format(
                            urc + int(collect_index_from))

                        r = requests.get(j)
                        if r.status_code != 200 or r.status_code == 503 or r.status_code == 404 or r.status_code == 405:
                            continue
                        else:
                            linky = []
                            aa = newspaper(j)
                            linky.append(aa)
                            # linky.append(aa.article)
                            # linky.append(aa.keywords)
                            # linky.append(aa.authors)
                            # linky.append(aa.filename)
                            # linky.append(aa.category)
                            # linky.append(aa.summary)
                            # if aa.summary==None:
                            #     print("bobbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
                            #     pass
                            # else:

                            with open(collect_data_to, 'a', encoding='UTF8', newline='') as csvfile:
                                csvwriter = csv.writer(csvfile,
                                                       delimiter=';')  # , quotechar='|', quoting=csv.QUOTE_MINIMAL
                                # csvwriter.writerow(['links'])
                                count += 1
                                print("********************************")
                                print(count)
                                print("********************************")
                                for lin in linky:
                                    csvwriter.writerow(
                                        [lin.filename, lin.date_publish[:-9], lin.category, lin.language, lin.headline,
                                         lin.article])



                    except(
                            requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,
                            requests.exceptions.InvalidURL,
                            requests.exceptions.InvalidSchema, requests.exceptions.ConnectTimeout):
                        continue



    else:
        pass
    return render(request, 'index5.html', {"collect_article_result": collect_article_result})







#--------------------------end of collectin article ------------------------------------




#********************** spacy ex*******************************
def spacyex(request):
    myarr=[]
    stext = request.GET.get("spacy-text")
    with open(stext) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if row == 0:
                pass
            else:
                myarr.append(row)
    print("Reading from file is completed ")

    # doc = nlp(stext)
    #
    # # Analyze syntax
    # np="Noun phrases:{}".format( [chunk.text for chunk in doc.noun_chunks])
    # nv="Verbs:{}".format( [token.lemma_ for token in doc if token.pos_ == "VERB"])
    #
    # # Find named entities, phrases and concepts
    # lab=[]
    # lab2=[]
    # for entity in doc.ents:
    #     print(entity.text, entity.label_)
    #     lab.append(entity.label_)
    #     lab2.append(entity.text)
    #
    #
    # spacy_result=lab
    # spacy_result2 = lab2
    # spacy_resultnp=np
    # spacy_resultnv=nv




################################################################################
    # stext="/home/bilgi/Desktop/dene.txt"
    # raw_tweets = pd.read_json(stext, lines=True)
    # # result3 = "successfully completed with {} results".format(len(raw_tweets))
    # users = json_normalize(raw_tweets['user'])
    # users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
    # users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
    # # Create DataFrame and remove duplicates
    # users = pd.DataFrame(users)
    # # users.drop_duplicates(subset=['userId'], inplace=True)
    # # Transform 'raw_tweets' DataFrame
    # # Add column for 'userId'
    # user_id = [user['id'] for user in raw_tweets['user']]
    # raw_tweets['userId'] = user_id
    # # Remove less important columns
    # cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
    #         'quoteCount']
    # tweets = raw_tweets[cols]
    # tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
    # cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
    #         'location']
    # use = users[cols]
    # twts = use.merge(tweets, on='userId')
    # stextc=stext+"c"
    # twts.to_csv(stextc, index=False)
    # # tweets_df4.to_csv(filname4 ,index=False)
    #
    # df = pd.read_csv(stextc)
    # df
    spacy_result=myarr
    return render(request, 'index5.html', {"spacy_result": spacy_result})
    # return render(request, 'index5.html', {"spacy_result": spacy_result,"spacy_result2": spacy_result2,"spacy_resultnp": spacy_resultnp,"spacy_resultnv": spacy_resultnv})
#---------------------------------------------------#