import requests
from bs4 import BeautifulSoup

while True:

    url = "https://www.trendyol.com/poco/x4-pro-5g-256-gb-siyah-cep-telefonu-xiaomi-turkiye-garantili-p-270352357?boutiqueId=61&merchantId=106203"


    page = requests.get(url)

    htmlPage = BeautifulSoup(page.content,"html.parser")



    ## Telegram

    from datetime import datetime
    import time

    ap = "https://api.telegram.org/bot5499857368:AAFrLB4kvnIc8kW4jy64w1xFGICxksNL7o0/SendMessage"



    productTitle = htmlPage.find("h1",class_="pr-new-br").getText()

    price = htmlPage.find("span",class_="prc-dsc").getText()

    mesaj = productTitle

    print(productTitle)
    print(price)

    requests.post(url=ap,data={"chat_id":"1909392259","text":productTitle + " \n " + price }).json()

    time.sleep(5)
