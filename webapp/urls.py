"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# import webapp.webapp.views
from .views import *
import re
from django.urls import path
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from django.conf.urls.static import static

from .settings import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home_view),
    path('index.html',index),
    path('index2.html',index2),
    path('index3.html',index3),
    path('index4.html',index4),
    path('',index5),
    path('kill',kill,name="kill"),
    path('header.html',header),
    path('navbar.html',navbar),
    path('footer.html',footer),
    path('brows.html',brows),
    path('contact.html',contact),
    path('about.html',about),
    path('signin.html',signin),
    path('signup.html',signup),
    path('sidebar-left.html',sidebarleft),
    path('sidebar-right.html',sidebarright),
    path('portfolio-details.html',portfoliodetails),
    path('googlesearch.html',googlesearch),
    path('add', add, name="add"),
    path('upload/',download_file,name='download_file'),
    path('g_upload/',download_file_g,name='download_file_g'),
    path('add_google_detail', add_google_detail , name="add_google_detail"),
    path('topic_google_add',topic_google_add,name="topic_google_add"),
    path('bing_add',bing_add,name="bing_add"),
    path('bing_add_detail',bing_add_detail,name="bing_add_detail"),
    path('components.html',components),
    path('collect_article',collect_article,name="collect_article"),
    path('complex_snscrape',complex_snscrape,name="complex_snscrape"),
    path('simple_snscrape',simple_snscrape,name="simple_snscrape"),
    path('search_tweepy_query',search_tweepy_query,name="search_tweepy_query"),
    path('search_tweepy_timeline',search_tweepy_timeline,name="search_tweepy_timeline"),
    path('search_tweepy_geo',search_tweepy_geo,name="search_tweepy_geo"),
    path('faceb',faceb,name="faceb"),
    path('search_reddit',search_reddit,name="search_reddit"),
    # path('search_facebook',search_facebook,name="search_facebook"),
    path('open_dtale',open_dtale,name="open_dtale"),
    path('spacyex',spacyex,name="spacyex"),
    path('newspaper_search',newspaper_search,name="newspaper_search"),
    path('newspaper_search_all',newspaper_search_all,name="newspaper_search_all"),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.DOWNLOAD_G_ROOT}),
    # path('loading/',ResultView.ajax_view,name="loading"),



]
# +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
if settings.DEBUG:
  urlpatterns += static(settings.DOWNLOAD_G_URL, document_root=settings.DOWNLOAD_G_ROOT) #If uploading is the only thing, and the file is not meant to be displayed or read, you don't need to add this
