from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

BUDGET = 35.00
my_email = "your email here"
password = "your password here"

# A valid amazon link here
url = "https://www.amazon.com/Logitech-Gaming-Backlit-Programmable-Buttons/dp/B0086UK7IQ/?_encoding=UTF8&pd_rd_w=oziLB&content-id=amzn1.sym.10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_p=10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_r=9HD0FAWPTQHZ51MBFJEW&pd_rd_wg=z7Bhc&pd_rd_r=75ff02c2-69a5-4c56-ac4b-8e58c9f59ec9&ref_=pd_gw_exports_top_sellers_unrec"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en,en-US;q=0.9,es;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",

}

response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, "lxml")
price = float(soup.select("td span span")[0].get_text()[1:])
print(price)

if price < BUDGET:
    print("Buy it!")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Buy it! The price is below {BUDGET}",
        )
