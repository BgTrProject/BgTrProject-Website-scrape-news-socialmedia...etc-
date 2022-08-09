from webapp.pycode.news import newspaper
import requests
import csv
import time
# import datetime
myarr=[]
path2="/home/bilgi/Desktop/zzdd.txt"
path="/home/bilgi/Desktop/zzzzbing.csv"
filename="/home/bilgi/Desktop/bing_search_content.csv"
with open(path2) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        if row==0:
            pass
        else:
            myarr.append(row)
print("Reading from file is completed ")
###############3 csv header####################333
with open(filename, 'a', encoding='UTF8', newline='') as csvfileh:
    csvwriterh = csv.writer(csvfileh, delimiter=';')  # , quotechar='|', quoting=csv.QUOTE_MINIMAL
    csvwriterh.writerow(['url','publish_date','category','language','headline','article'])
count=0
urc=0
for i in myarr[4137:]:
    for j in i:
        t1=time.time()
        rr=requests.get(j)
        t2=time.time()
        tt=t2-t1

        if rr.status_code!=200 or rr.status_code==503 or tt>60:
            print("50000000000003333333333333333")
            time.sleep(3)
            continue
        else:

            try:
                urc+=1
                print("-------------")
                print(urc)
                print("-------------")

                r = requests.get(j)
                if r.status_code!=200 or r.status_code==503 or r.status_code==404 or r.status_code==405:
                    continue
                else:
                    linky=[]
                    aa=newspaper(j)
                    print("******************")
                    print(aa.filename)
                    leng=len(aa.article)
                    print(type(leng))
                    print(leng)
                    print("******************")
                    if leng>70:
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

                        with open(filename, 'a', encoding='UTF8', newline='') as csvfile:
                            csvwriter = csv.writer(csvfile, delimiter=';') #, quotechar='|', quoting=csv.QUOTE_MINIMAL
                            # csvwriter.writerow(['links'])
                            count+=1
                            print("********************************")
                            print(count)
                            print("********************************")
                            for lin in linky:
                                csvwriter.writerow([lin.filename,lin.date_publish[:-9],lin.category,lin.language,lin.headline,lin.article])
                    else:
                        pass

            except(
             requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL,
             requests.exceptions.InvalidSchema,requests.exceptions.ConnectTimeout,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout,requests.exceptions.BaseHTTPError):
                 continue