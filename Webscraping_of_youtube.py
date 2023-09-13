from pytube import YouTube
import requests as req
from bs4 import BeautifulSoup
from collections import Counter
import scrapetube as s
video="https://www.youtube.com/watch?v=1qmPNot9NJs"
x=YouTube(video)
cid=x.channel_id
#print(cid)
v=s.get_channel(cid)
links=[]
date=[]
for i in v:
    d=Counter(i['videoId'])
    url="https://www.youtube.com/watch?v="+str(i['videoId'])
    r=req.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    date_element = soup.find("meta", itemprop="uploadDate")
    #print(date_element)
    upload_date_iso = date_element["content"]
    print(upload_date_iso)
    u = upload_date_iso.split("T")[0].replace("-", " ").split(" ")
    if int(u[0])==2022 or int(u[0])==2023:
        if int(u[0])==2022:
            if int(u[1])>=8:
                if int(u[1])==8:
                    if int(u[2])>=8:
                        if  u not in date:
                            date.append(u)
                            links.append(url)
                else:
                    if u not in date:
                        date.append(u)
                        links.append(url)
        else:
            if int(u[1])<=5:
                if int(u[1])==5:
                    if int(u[2])<=22:
                        if u not in date:
                            date.append(u)
                            links.append(url)
                else:
                    if u not in date:
                        date.append(u)
                        links.append(url)
    if url in links:
        K = max(zip(d.values(), d.keys()))
        print(str(K[1])+str(K[0]))
