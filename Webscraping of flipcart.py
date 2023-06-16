import requests as req
from bs4 import BeautifulSoup
import pandas as pd
product=[]
description=[]
offer_Price=[]
original_price=[]
offer_percentage=[]
for i in range(1,21):   #taken datails of 20 pages
    url="https://www.flipkart.com/search?q=watches+for+mens&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r=req.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find_all("div",class_="_1xHGtK _373qXS")
    for j in box:
        pro_names=j.find("div",class_="_2WkVRV")
        descr = j.find("a", class_="IRpwTa")
        f_price = j.find("div", class_="_30jeq3")
        o_price = j.find("div", class_="_3I9_wc")
        offer_per = j.find("div", class_="_3Ay6Sb")
        product.append(pro_names.text)
        description.append(descr.text)
        if o_price is None and offer_per is None:
            original_price.append((f_price.text)[1:])
            offer_Price.append((o_price))
            offer_percentage.append(offer_per)
        else:
            original_price.append((o_price.text)[1:])
            offer_Price.append((f_price.text)[1:])
            if offer_per is None:
                offer_percentage.append(offer_per)
            else:
                offer_percentage.append(offer_per.text)
print(len(product),len(description),len(offer_Price),len(original_price),len(offer_percentage)) #All the length should be equal
df=pd.DataFrame({"Product Name":product,"Product Decription":description,"Offer Pricec":offer_Price,"Original Price":original_price,"Offer percentage":offer_percentage})
df.to_csv("Watches for men.csv")
