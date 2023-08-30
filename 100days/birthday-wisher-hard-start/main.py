##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import pandas
import datetime as dt
import random

my_email="theanuragkmr@yahoo.com"
password="xmoafqzrspfelfje"

today=(dt.datetime.now().month,dt.datetime.now().day)

data=pandas.read_csv("birthdays.csv")

birthday_dict={
    (row["month"],row["day"]):row for (index,row) in data.iterrows()
}

if today in birthday_dict:
    placeholder="[NAME]"
    name=birthday_dict[today]
    path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(path) as f:
        contents=f.read()
        contents=contents.replace(placeholder,name["name"])
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=name["email"],
                            msg=f"subject: Happy bithday!!\n\n{contents}"
#                             )
# d=pandas.DataFrame(birthday_dict)
# print(d)