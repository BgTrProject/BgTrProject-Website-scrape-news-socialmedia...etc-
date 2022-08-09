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

![](/resimler/tweepy1.png)

Tweepy modulu kullanılarak arama gerçekleştirme:
Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
İlgili arama kelimesi (keyword) ve istenilen sonuçtan kaç adet talep edileceği (max result) ve hangi
dilde arama yapılacağı girildikten sonra ilgili sonuçların hangi dosya adında kaydedileceği (file name)
belirtip arama (search) butonuna tıklanır.





![](/resimler/tweet2.png)

Tweepy modülünü kullanarak zaman şeridi üzerinde arama yapma:
Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
İlgili zaman şeridi sonucu için sadece istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin
girilmesi yeterlidir. Daha sonra indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip
arama (search) butonu tıklanır.


![](/resimler/tweepy3.png)

Tweepy modülünü kullanarak coğrafik arama yapma:
Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
Apinin modulunun coğrafik araması belirtilen cografik kod ait lokasyonda atılmış olan tweetleri
toplar. İlgili cografik kod (geo code) girilmesi ve indirilecek dosyaların hangi isimde kaydedileceği (file
name) belirtilip arama (search) butonu tıklanır.


![](/resimler/snscrape.png)

Snscrape Modulu:
Snscrape, sosyal ağ hizmetleri için bir (scraper) kazıyıcıdır. Kullanıcı profilleri, hashtag’lar gibi şeyleri
aratır ve ilgili sonuçları (tweetleri) geri döndürür.
snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles,
hashtags, or searches and returns the discovered items, e.g. the relevant posts.
Basit arama (Simple Search snscrape):
Bu modülde ilgili istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin girilmesi akabinde
tarih (date) ve aranılacak kelime (keyword) girilip indirilecek dosyaların hangi isimde kaydedileceği
(file name) belirtilip arama (search) butonu tıklanır.
Karmaşık arama (Complex Search snscrape):
Bu modul iki farklı şekilde kullanılır. 1-keyworde göre arama 2-hashtage göre arama
1-keyworde göre arama:Bu modülde ilgili istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin girilmesi, hangi
dilde(language) arama yapılacağı seçimi yapılıp, akabinde tarih (date) ve aranılacak kelime (keyword)
girilip indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip arama (search) butonu
tıklanır.
2- hashtage göre arama:
Bu modülde ilgili istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin girilmesi, hangi
dilde(language) arama yapılacağı seçimi yapılıp, akabinde tarih (date) ve aranılacak hashtag başında
@ işareti ile girilip indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip arama
(search) butonu tıklanır.



![](/resimler/google.png)

Google Haber Arama (Google Search):
Googlede arama yapmak için tasarlanan bot ile normal kullanıcının Google arama motoruna girip
herhangi bir şeyi araması taklit edilerek oluşturuldu. Bu botun tasarımında selenium modülünden
faydalanılarak tasarlandı. Selenium botu sayesinde elde edilen linklerden gerekli haber yayınlanma
tarihi(published date), haber başlığı (news title) ve haber içeriği (news article) newsplease
kullanılarak csv formatında oluşturulan dosyaya kaydedilip ilgili dosya zip formatında sıkıştırılıp
kullanıcı bilgisayarına indirilip ilgili işlem son bulur.
Söz konusu bot aranılacak kelimeyi (keyword) , hangi gazetede aranılacağını (newspapers name) ,
belirtilen başlangıç tarihi ve sonlanma tarihleri (start date & finish date) akabinde indirilecek
dosyaların hangi isimde kaydedileceği (file name) belirtilip arama (search) butonu tıklanır. Bu sayede
selenium botu Chrome browserini açıp ilgili parametreleri (keyword, newspapers name, start
date,finish date) browserın arama kısmına yazıp, ilgili sonuçları elde eder ve her sayfadaki linkleri alıp
csv formatında dosyaya kaydeder.
Kaydedilmiş dosyadan haber detaylarının çekilmesi için newsplease modulu kullanıldı. Bu module
parametre olarak gönderilen adres (url) modülde işlenip çıktı olarak: haber yayınlanma
tarihi(published date), haber başlığı (news title) ve haber içeriği (news article) elde edilip. Bu çıktılar
csv formatında oluşturulan dosyaya kaydedilip ilgili dosya zip formatında sıkıştırılıp kullanıcı
bilgisayarına indirilir.



![](/resimler/google_news.png)

Google Konu endeksli Haber Arama (Topic News Search) :
Googlede arama yapmak için tasarlanan bot ile normal kullanıcının Google arama motoruna girip
herhangi bir şeyi araması taklit edilerek oluşturuldu. Bu botun tasarımında selenium modülünden
faydalanılarak tasarlandı. Selenium botu sayesinde elde edilen linklerden gerekli haber yayınlanma
tarihi(published date), haber başlığı (news title) ve haber içeriği (news article) newsplease
kullanılarak csv formatında oluşturulan dosyaya kaydedilip ilgili dosya zip formatında sıkıştırılıp
kullanıcı bilgisayarına indirilip ilgili işlem son bulur.
Söz konusu bot aranılacak kelimeyi (keyword) , hangi konunun aranılacağını (Topic name) , belirtilen
başlangıç tarihi ve sonlanma tarihleri (start date & finish date) akabinde indirilecek dosyaların hangi
isimde kaydedileceği (file name) belirtilip arama (search) butonu tıklanır. Bu sayede selenium botu
Chrome browserini açıp ilgili parametreleri (keyword, newspapers name, start date,finish date)
browserın arama kısmına yazıp, ilgili sonuçları elde eder ve her sayfadaki linkleri alıp csv formatında
dosyaya kaydeder.
Kaydedilmiş dosyadan haber detaylarının çekilmesi için newsplease modulu kullanıldı. Bu module
parametre olarak gönderilen adres (url) modülde işlenip çıktı olarak: haber yayınlanma
tarihi(published date), haber başlığı (news title) ve haber içeriği (news article) elde edilip. Bu çıktılar
csv formatında oluşturulan dosyaya kaydedilip ilgili dosya zip formatında sıkıştırılıp kullanıcı
bilgisayarına indirilir.



![](/resimler/bing.png)

Bing Haber Arama (Bing News Search):
Bing Arama motoru üzerinde yapılan aramaların haber linklerinin toplanması için stack veri yapısı
kullanılarak ram üzerinde fazla dinamik hafıza (heap) kullanımı engellenip Pythonun BeatifulSoup
modulunden yararlanılarak her sayfadaki haber linki toplanılıp .txt formatında muhtelif dosyaya
kaydedilip. Daha sonra newsplease modulunden yararlanıp ilgili haber linkine ait içerikler csv
formatında dosyaya kaydedilip son aşamada zip halinde sıkıştırılıp kullanıcı bilgisayarına indirilir.
Oluşturulmuş arayüzde görüldüğü üzere Bing haber araması için aranılacak kelime (keyword) ve hangi
haber sitesinde(newspaper name) arama yapılacağı ve son olarak toplanılacak linklerin hangi isimde
kaydedileceği (file name) parametreleri doldrulup Bing üzerinde Ara (Search on Bing) tuşuna tıklanılıp
ilgili haberlerle alakalı haber linklerinin (urls) elde edilir. Elde edilen haber linkleri ilgili isimde
oluşturulan .txt dosyasına kaydedilir.
Daha sonra txt dosyasından çağrılan haber linkleri newsplease parametre olarak verilir ve çıktı olarak:
haber yayınlanma tarihi(published date), haber başlığı (news title) ve haber içeriği (news article) elde
edilip. Bu çıktılar csv formatında oluşturulan dosyaya kaydedilip ilgili dosya zip formatında sıkıştırılıp
kullanıcı bilgisayarına indirilir.


![](/resimler/newspaper.png)

Gazetelerde Keyworde Göre Haber Arama:
Hergazetenin yapısı farklı olduğundan vede farklı dillerde farklı şekiller kodlandığından çoğu ulusal
haber kaynaklarının içerikleri newsplease gibi scraperlar tarafından eksik olarak işlenip eksik verilerin
oluşmasına neden olduğundan . Belirlediğimiz çeşitli ulusal gazetelerin yapıları tek tek incelenip
kimisini gerek Python BeatifulSoup gereksede selenium’dan faydalanarak kendi yapılarına uygun
kodlar ile ayrı ayrı modüller geliştirdik.Bu sayede Bu haber sitelerinin içeriklerinden verimli bir şekilde
faydalanmayı başardık Bu gazetelerden bazıları:
DailyHurriyet,dailySabah,Haberler,sabah,takvim,turkiyegazetesi,vatan….
Aranılacak kelime (keyword), gazete ismi (newspaper name) ve akabinde indirilecek dosyaların hangi
isimde kaydedileceği (file name) belirtilip tarihe göre arama (search by date) butonu tıklanır. Bu
sayede gönderilen parametreler yazmış olduğumuz modul ile hangi gazete ismi ile arama yapılmış ise
o sınıfı bulup o sınıfa ait başlangıç değer atamalarını (initialize) atayıp sınıf içerisinde tarih oluşturma
(Date Creator) fonksiyonu ile ilgili gazete url ine uygun formattaki tarihi oluşturup bu sayede haber
linki elde etme (Get Link) fonksiyonunu çağırıp ilgili tarihteki gazete linkleri elde ediliyor. Toplanılan
linklerden haber içeriklerinin alınması için ilgili fonksiyon olan (Creator) ile elde edilip sözkonusu
sonuçlar .txt formatında dosyaya kaydedilip son aşamada da bu dosya zip formatında sıkıştırılıp
kullanıcı bilgisayarına indiriliyor.


![](/resimler/newspaper2.png)

Gazetelerde Tüm Haber Arama:
Hergazetenin yapısı farklı olduğundan vede farklı dillerde farklı şekiller kodlandığından çoğu ulusal
haber kaynaklarının içerikleri newsplease gibi scraperlar tarafından eksik olarak işlenip eksik verilerin
oluşmasına neden olduğundan . Belirlediğimiz çeşitli ulusal gazetelerin yapıları tek tek incelenip
kimisini gerek Python BeatifulSoup gereksede selenium’dan faydalanarak kendi yapılarına uygun
kodlar ile ayrı ayrı modüller geliştirdik.Bu sayede Bu haber sitelerinin içeriklerinden verimli bir şekilde
faydalanmayı başardık Bu gazetelerden
bazıları:aa,banker,bgnes,cumhuriyet,dailymail,dailysabah,dnevnik,duvar,dwnews,ensonhaber,evrens
el,guardian,haberler,hürriyet, independent,memurlar,milli,odatv4,sabah,sega,sozcu,trud,turkiye…vb
Başlangıç tarihi (start date) , sonlanma tarihi (finish date), kategory (bu parametre gazeteden
gazeteye göre değişmekle beraber şöyle ki: girilen kategory aranılan gazetede mevcutsa spesifik
olarak o kategoride haber araması yapar aksi taktirde tüm sonuçları döndürür.), gazete ismi
(newspaper name) ve akabinde indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip
tarihe göre arama (search by date) butonu tıklanır. Bu sayede gönderilen parametreler yazmış
olduğumuz modul ile hangi gazete ismi ile arama yapılmış ise o sınıfı bulup o sınıfa ait başlangıç değer
atamalarını (initialize) atayıp sınıf içerisinde tarih oluşturma (Date Creator) fonksiyonu ile ilgili gazete
url ine uygun formattaki tarihi oluşturup bu sayede haber linki elde etme (Get Link) fonksiyonunu
çağırıp ilgili tarihteki gazete linkleri elde ediliyor. Toplanılan linklerden haber içeriklerinin alınması
için ilgili fonksiyon olan (Creator) ile elde edilip sözkonusu sonuçlar .txt formatında dosyaya
kaydedilip son aşamada da bu dosya zip formatında sıkıştırılıp kullanıcı bilgisayarına indiriliyor.
