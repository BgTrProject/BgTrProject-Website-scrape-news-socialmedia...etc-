# BgTrProject-Website
 1- Download ettikten sonra sanalortamı kurup çalıştırın.
 linux için kod : source venv/bin/activate
 2- gerekli kütüphanelerin kurulumu için requirements dosyasını çalıştırın.
 pip install -r requirements.txt
 3- projenin çalıştırılması için 
 python manage.py runserver
 
iyi çalışmalar ....

Arayüzdeki modullerin kullanımı için :


Tweepy modülü:

![alt text](https://github.com/BgTrProject/BgTrProject-Website-scrape-news-socialmedia...etc-/tree/main/resimler/tweepy1.png?raw=false)

Tweepy modulu kullanılarak arama gerçekleştirme:
Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
İlgili arama kelimesi (keyword) ve istenilen sonuçtan kaç adet talep edileceği (max result) ve hangi
dilde arama yapılacağı girildikten sonra ilgili sonuçların hangi dosya adında kaydedileceği (file name)
belirtip arama (search) butonuna tıklanır.

