import requests
from datetime import datetime
import smtplib
import time

my_lat=28.351839
my_log=79.409561

def iss_over_head():

    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    iss_lat=float(data["iss_position"]["latitude"])
    iss_log=float(data["iss_position"]["longitude"])

    #My position with -5 and +5

    if my_lat-5<=iss_lat<=my_lat+5 and my_log-5<=iss_log<=my_log+5:
        return True


def is_night():
    parameters={
        "lat":my_lat,
        "long":my_log,
        "formatted":0,
    }


    response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split(":")[0].split("T")[1])
    sunset=int(data["results"]["sunset"].split(":")[0].split("T")[1])

    time_now=datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True


my_email="theanuragkmr@yahoo.com"
password="xmoafqzrspfelfje"

while True:
    time.sleep(60)
    if iss_over_head() and is_night():
        connection=smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg="Subject:Look up!!\n\nIss is above you in the sky!! ")