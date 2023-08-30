import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
url="https://www.amazon.in/iQOO-Snapdragon-Segment-Purchased-Separately/dp/B07WDK3ZS6?content-id=amzn1.sym.b08536cf-f878-4c12-89ee-75b9dc3e1be5"

headers = { 'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
          }

response=requests.get(url=url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
title=soup.find("span",id="productTitle").getText().strip()
span_price=soup.find("span",class_="a-offscreen")
coma_price=span_price.getText().split("₹")[1].split(".")[0]
price=float(coma_price.replace(",",""))
print(title)
print(price)
buy_price=14999.0
if price<buy_price:
    message=f"Mobile is lost as {coma_price}"
    with SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user="thenanuragkmr@yahoo.com",password="Mannu123@")
        connection.sendmail(from_addr="thenanuragkmr@yahoo.com",
                            to_addrs="thenanuragkmr@yahoo.com",
                            msg=f"Subject: {title} Price Alert\n\nThe Product Price is now ${price}, below your target price. Buy Now!")