import datetime as dt
import smtplib
from random import choice

my_email = "your email here"
password = "not so fast xd"  # password here

now = dt.datetime.now()

if now.strftime("%A") == "Saturday":
    with open("quotes.txt") as f:
        lines = f.readlines()
    # This connects to the gmail service, this works in order to send a mail
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Starts Transport Layer Security, which encrypts the mail
        connection.starttls()
        # Login using email and password
        connection.login(user=my_email, password=password)
        # Then send the mail
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Motivational quote!\n\n{choice(lines)}"
        )
