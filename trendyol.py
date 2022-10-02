from bs4 import BeautifulSoup
import requests

while True:
    url = "https://www.trendyol.com/nike/academy-team-s-futbol-spor-cantasi-cu8097-010-p-101456942"


    sayfa = requests.get(url)

    html_sayfa = BeautifulSoup(sayfa.content,"html.parser")



    isim = html_sayfa.find("h1",class_="pr-new-br").getText()

    print(isim)

    fiyat = html_sayfa.find("span",class_="prc-dsc").getText()

    print(fiyat)


    #Telegram

    import time


    api = "https://api.telegram.org/bot-ID-/SendMessage"

    mesaj = isim + "\n" + fiyat

    requests.post(url=api,data={"chat_id":"1909392259","text":mesaj}).json()

    time.sleep(5)





