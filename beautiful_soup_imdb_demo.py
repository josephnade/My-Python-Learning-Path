url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

import requests
from bs4 import BeautifulSoup

html = requests.get(url).content
number = int(input("How many film do you want to see ="))
print("IMDb Top 250 Movies".center(50,"*"))
soup = BeautifulSoup(html,'html.parser')
list = soup.find("tbody",{"class": "lister-list"}).find_all("tr",limit=number)
c=1
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").string
    year = tr.find("td",{"class" : "titleColumn"}).find("span").string
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").string
    print(f"{c}. {title} {year}IMDB Rating:{rating} ")
    c+=1
