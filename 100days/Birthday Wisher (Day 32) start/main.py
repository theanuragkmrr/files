import smtplib
import datetime as dt
import random

my_email="theanuragkmr@yahoo.com"
password="xmoafqzrspfelfje"
now=dt.datetime.now()
weekday=now.weekday()
if weekday==3:
    with open("quotes.txt") as f:
        qoutes=f.readlines()
        q=random.choice(qoutes)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="theanuragkmr@gmail.com",
                            msg=f"subject:motivation\n\n{q}")