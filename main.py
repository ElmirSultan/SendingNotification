import requests
import lxml
import smtplib
from bs4 import BeautifulSoup
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41",
    "Accept-Language":"en-US,en;q=0.9"
}

response = requests.get(URL,headers=header)
my_target = 100
my_email = "YOUR EMAIL"
password = "EMAIL PASSWORD"

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < my_target:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="EMAIL THAT YOU WANT TO SEND NOTIFICATION",
                            msg=f"You can buy this product now it is {price_as_float}")

