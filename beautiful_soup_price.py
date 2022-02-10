n11_laptop_url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

import requests
from bs4 import BeautifulSoup

html = requests.get(n11_laptop_url).content
soup = BeautifulSoup(html, "html.parser")
list = soup.find("div",{"class":"listView"}).ul.find_all("li",{"class":"column"})
for entity in list:
    title = entity.div.div.a.get("title")
    price = entity.div.find("div",{"class":"proDetail"}).ins.text.strip().strip("TL").strip()
    print(f"{title} Price:{price} TL")
