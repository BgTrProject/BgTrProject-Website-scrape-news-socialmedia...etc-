from django.shortcuts import render,HttpResponse
import os
import sys
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from pycode.news import newspaper
from six.moves import urllib
import requests
import csv
import json
import json_normalize
import pandas as pd
import dtale
import time
from datetime import datetime
from datetime import timedelta
import numpy as np
from tweepy import *
import tweepy as tw

from pycode.google import google_search
from pycode.google6 import google_search6
from pycode.bing import Bing
from pycode.google7 import google_search7
from pycode.google8 import google_search8



#
# def upload(request):
#     return render(request,'upload',{})

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
    downloadurl=""


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
            filname = desktop[:-7] + "/websites/rubic/webapp/upload/" + ff
            downloadurl = filname
            print(filname)
            os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} lang:{}"> {}'
                      .format(tweet_count, since_date, text_query, fromuser, lang, filname))
            filname8 = str(filname)
            raw_tweets = pd.read_json(filname8, lines=True, encoding='utf-8')
            raw_tweets.to_csv(filname8, index=None)
            # down_url=filname8
            # dest_url="E://{}".format(mm)
            # urllib.request.urlretrieve(down_url,dest_url)


            # n_filname="file://"+dest_url
            df = pd.read_csv(filname8)
            d = dtale.show(df)
            d.open_browser()
            result_c_s = "successfully completed"
            # result_c_s = "successfully completed with {} results".format(len(raw_tweets))
            print(result_c_s)
            return render(request, 'index5.html', {"result_c_s": result_c_s})


        except:
            print("pathway problem occurred for complex search . Please check your pathway")
            pass
    else:
        print("nanay")
        # desktop2 = desktop.replace("Desktop", "Masaüstü")
        # ff = str(filname2)
        # filname2 = desktop2 + "//" + filname2
        # downloadurl2=filname2
        # # print(filname2)
        # print("**************************************")
        # os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} lang:{}"> {}'
        #           .format(tweet_count, since_date, text_query, fromuser, lang, filname2))
        # req = request.get(downloadurl2)
        # downloadurl2_ = req.url(downloadurl2)
        # print("###################################")
        # print(downloadurl2_)
        # print(downloadurl2)
        # print("###################################")
        # with open(downloadurl2_,'a') as f2:
        #     for chunk in req.iter_content(chunk_size=8192):
        #         if chunk:
        #             f2.write(chunk)
        # # raw_tweets = pd.read_json(filname2, lines=True)
        # # # result3 = "successfully completed with {} results".format(len(raw_tweets))
        # # users = json_normalize(raw_tweets['user'])
        # # users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
        # # users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
        # # # Create DataFrame and remove duplicates
        # # users = pd.DataFrame(users)
        # # # users.drop_duplicates(subset=['userId'], inplace=True)
        # # # Transform 'raw_tweets' DataFrame
        # # # Add column for 'userId'
        # # user_id = [user['id'] for user in raw_tweets['user']]
        # # raw_tweets['userId'] = user_id
        # # # Remove less important columns
        # # cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
        # #         'quoteCount']
        # # tweets = raw_tweets[cols]
        # # tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
        # # cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
        # #         'location']
        # # use = users[cols]
        # # twts = use.merge(tweets, on='userId')
        # # twts.to_csv(filname2, index=False)
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

####################################### simple snscrape ##############################

def simple_snscrape(request):
    tweet_count2 = request.GET.get("tweet_count2")
    since_date2 = request.GET.get("since_date2")
    text_query2 = request.GET.get("text_query2")
    filname4 = request.GET.get("filname4")
    fn=str(filname4)
    filname4 = fn + ".csv"
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
            filname4 = desktop + "/" + ff

            print("------------------")
            print(filname4)
            print("------------------")
            os.system(
                "snscrape --jsonl --progress --max-results {} --since {} twitter-search '{}'> {}".format(
                    tweet_count2, since_date2, text_query2, filname4))
            filname44 = str(filname4)
            raw_tweets = pd.read_json(filname44, lines=True, encoding='utf-8')
            raw_tweets.to_csv(filname44, index=None)
            df = pd.read_csv(filname44)
            d = dtale.show(df)
            d.open_browser()
            result_s_s = "successfully completed with {} results".format(len(raw_tweets))
            # result_s_s = "successfully completed with {} results"
            print(result_s_s)
            return render(request, 'index5.html', {"result_s_s": result_s_s})


    # return render(request, 'index5.html', {"result_s_s": result_s_s})


        except:
            print("pathway problem occurred for simple search. Please check your pathway")
            pass
    else:
        desktop2 = desktop.replace("Desktop", "Masaüstü")
        ff = str(filname5)
        filname5 = desktop2 + "//" + filname5
        os.system(
            "snscrape --jsonl --progress --max-results {} --since {} twitter-search '{}'> {}".format(
                tweet_count2, since_date2, text_query2, filname5))
        # tweets_df5 = pd.read_json(filname5, lines=True,encoding='utf-8')

        raw_tweets = pd.read_json(filname5, lines=True, encoding='utf-8')
        # raw_tweets=tweet
        users = json_normalize(raw_tweets['user'])
        users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
        users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
        # Create DataFrame and remove duplicates
        users = pd.DataFrame(users)
        # users.drop_duplicates(subset=['userId'], inplace=True)
        # Transform 'raw_tweets' DataFrame
        # Add column for 'userId'
        user_id = [user['id'] for user in raw_tweets['user']]
        raw_tweets['userId'] = user_id
        # Remove less important columns
        cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
                'quoteCount']
        tweets = raw_tweets[cols]
        tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
        cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
                'location']
        use = users[cols]
        twts = use.merge(tweets, on='userId')
        twts.to_csv(filname5, index=False)
        df = pd.read_csv(filname5)
        d = dtale.show(df)
        d.open_browser()

        # tweets_df5.to_csv(filname5 ,index=False)
        result_s_s = "successfully completed with {} results".format(len(twts))
        print(result_s_s)
        return render(request, 'index5.html', {"result_s_s": result_s_s})

#---------------------------------- end of simple snscrape ---------------------------


##################################### facebook #########################################

def search_facebook(request):
    pass

#------------------------------end of facebook ------------------------------------------------

##################################### reddit #########################################

def search_reddit(request):
    pass

#------------------------------end of reddit ------------------------------------------------

################################################################### part 2 #############################################

####################################### google all search   ############################
def add(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    fname = request.GET.get("fname")
    date1 = request.GET.get("date1")
    date2 = request.GET.get("date2")
    # fname=fname+'.csv'

    vord_add = num1.split(',')
    links_add = num2.split(',')

    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        fname = desktop+ "/" + fname + '.csv'
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h = os.getcwd()
    fname2 = fname
    ######################### for linux
    if (h.startswith("/home")):
        for vord in vord_add:
            non = 0
            vord = vord.strip()

            for plink in links_add:
                plink = plink.strip()

                google = google_search8(vord, plink, fname, date1, date2)
                try:
                    for i in google.urls:
                        non += 1
                except AttributeError:
                    pass

        result = "Your search on google by website finished successfully with {} links".format(non)
        df2 = pd.read_csv(fname)
        ddf2 = dtale.show(df2)

        ddf2.open_browser()

        return render(request, 'index.html', {"result": result})
    ##################   for   windows
    else:
        for vord in vord_add:
            non = 0
            vord = vord.strip()

            for plink in links_add:
                plink = plink.strip()

                google = google_search8(vord, plink, fname, date1, date2)
                try:
                    for i in google.urls:
                        non += 1
                except AttributeError:
                    pass

        result = "Your search on google by website finished successfully with {} links".format(non)
        df2 = pd.read_csv(fname)
        ddf2 = dtale.show(df2)

        ddf2.open_browser()

        return render(request, 'index.html', {"result": result})

#####---------------------------  end of    google all search    ---------------------------------




##########################      google detail search      ######################

def add_google_detail(request):
    num1_det = request.GET.get("num1_det")
    num2_det = request.GET.get("num2_det")
    aralik_det=request.GET.get("aralik_det")
    fname_det = request.GET.get("fname_det")
    date1_det = request.GET.get("date1_det")
    date2_det = request.GET.get("date2_det")
    mydates2=datecreator(date1_det,date2_det,aralik_det)

    h=num1_det.split(',')
    z=num2_det.split(',')

    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    hos = os.getcwd()
    fname_det2=fname_det
    ######################### for linux
    if (hos.startswith("/home")):
        fname_det = desktop + "/" + fname_det + '.csv'
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
        google_detail_result = "Your search on google by website finished successfully with {} links".format(non)
        df2 = pd.read_csv(fname_det)
        ddf2 = dtale.show(df2)

        ddf2.open_browser()

        return render(request, 'index.html', {"google_detail_result": google_detail_result})


        ##########################    for windows
    else:
        fname_det2 = desktop + "//" + fname_det2 + '.csv'
        for vord in h:
            vord = vord.strip()

            for plink in z:
                plink = plink.strip()

                for j in range(len(mydates2) - 1):
                    google = google_search7(vord, plink, fname_det, mydates2[j], mydates2[j + 1])
                    non = 0
                    try:
                        for i in google.urls:
                            non += 1
                    except AttributeError:
                        pass
        google_detail_result = "Your search on google by website finished successfully with {} links".format(non)
        df2 = pd.read_csv(fname_det)
        ddf2 = dtale.show(df2)

        ddf2.open_browser()

        return render(request, 'index.html', {"google_detail_result": google_detail_result})

###--------------------------end  of ----------------- google detail search      -------------##



##################################       google topic  ###################################

def topic_google_add(request):
    btnum1 = request.GET.get("btnum1")
    btnum2 = request.GET.get("btnum2")
    btfname = request.GET.get("btfname")
    btdate1 = request.GET.get("btdate1")
    btdate2 = request.GET.get("btdate2")

    vord_bing = btnum1.split(',')
    links_bing = btnum2.split(',')

    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)
    except:
        print("Linux Veya Unix Yolu Bulunamadı")
    h_bing = os.getcwd()
    btffname2 = btfname
    ######################### for linux
    if (h_bing.startswith("/home")):
        noc = 0
        btfname = desktop + "/" + btfname + '.csv'
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
    # return render(request, 'index.html', {"topic_result": topic_result})
    ################ for window
    else:
        noc = 0
        btfname = desktop + "/" + btfname + '.csv'
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

    # df2 = pd.read_csv(fname_det)
    # ddf2 = dtale.show(df2)
    #
    # ddf2.open_browser()
    return render(request, 'index.html', {"topic_result": topic_result})



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
    bfname = request.GET.get("bfname")
    # bdate1 = request.GET.get("bdate1")
    # bdate2 = request.GET.get("bdate2")
    bresult="None"

    if bnum1!=None and bnum2!=None:
        bingsearch=Bing(bnum1, bnum2,bfname)
        bingsearch.crawl_all()
        bing_result="Bing search completed successfully"

    else:
        pass
    return render(request,'index.html',{"bing_result":bing_result})
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

        df2 = pd.read_csv(bing_fname_det)
        ddf2 = dtale.show(df2)
        ddf2.open_browser()


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

    return render(request, 'index.html', {"bing_detail_result": bing_detail_result})

#****************    end of   bing detail search    ***************************


################################ factiva #########################################################

def search_factiva(request):
    pass
#---------------------------- end of factiva ---------------------------------------------------


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
    return render(request, 'index.html', {"collect_article_result": collect_article_result})

#--------------------------end of collectin article ------------------------------------
