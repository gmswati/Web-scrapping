import json
from textwrap import indent
import requests
from bs4 import BeautifulSoup

with open("Task_1.json","r") as f:
    r = f.read()
    data = json.loads(r)
# print(data)

for movie in data:
    link=movie['Movie_url']
    sample_2=requests.get(link)
    # print(sample_2)
    soup_2=BeautifulSoup(sample_2.text,"html.parser")
    # print(soup_2)
    box=soup_2.find("div",class_="col mob col-center-right col-full-xs mop-main-column")
    print(box)
    sub = box.find("div",class_ = "thumbnail-scoreboard-wrap").p.get_text()
    year = sub[:4]
    movie["year"]= year
    # break

# print(data)

f=open("Task_1.1.json","w")
json.dump(data,f,indent=4)
# print(year)
