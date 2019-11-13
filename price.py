import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.ebay.es/p/Apple-iPhone-8-Plus-256GB-Plata-Libre/6027174329?iid=264351473201'
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

def check_price():
        page =requests.get(URL,headers = headers)
        soup = BeautifulSoup(page.content,'html.parser')
        #bs = BeautifulSoup(URL.read(),'lxml')

        price = soup.find("span",{"class":"item-price"}).get_text()
        converted_price = price[0:3]

        print(converted_price)

        if (int(converted_price) > 500):
            send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('abc@gmail.com','password') # write the mail address and your password here  
    subject = 'Price fell down!'
    body = 'Check the link'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'abcd@gmail.com', #from mail address
        'xyz@gmail.com', # to mail address
        msg
    )
    print('HEYYYYYYYYYYYYYYYY EMAIL SENT')

    server.quit()

check_price()

