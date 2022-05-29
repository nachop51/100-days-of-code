import datetime as dt
import pandas as pd
import smtplib
from random import randint


date = dt.datetime.now()
birthdays = pd.read_csv("birthdays.csv")
b_list = birthdays.to_dict(orient="records")

my_email = "your email here"
password = "your password here"

month = date.month
day = date.day

for dict in b_list:
    if dict['month'] == month:
        if dict['day'] == day:
            file_n = randint(1, 3)
            with open(f"letter_templates/letter_{file_n}.txt", "r") as file:
                lines = file.readlines()
            lines[0] = lines[0].replace("[NAME]", f"{dict['name']}")
            msg = "".join(lines)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(my_email, password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=dict['email'],
                    msg=f"Subject:Happy Birthday!\n\n{msg}"
                )
