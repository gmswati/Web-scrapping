from datetime import datetime
from textwrap import indent
import requests
import json
url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies"
sample=requests.get(url)
from bs4 import BeautifulSoup
soup=BeautifulSoup(sample.text,"html.parser")
def Scrap_Top_Movies():
    table=soup.find('table',class_='table')
    var=table.find_all('tr')
    Top_Movies=[]
    for var_1 in var:
        Movie_name=var_1.find_all('a',class_="unstyled articleLink")
        rank_1=var_1.find_all('td',class_="bold")
        rating=var_1.find_all('span',class_="tMeterScore")
        reviews=var_1.find_all('td',class_="right hidden-xs")
        Urls=var_1.find_all('a',class_="unstyled articleLink")


        i=0
        while i<len(rank_1):
            dict={}
            a=((rank_1[i].get_text()).strip())
            dict['Movie_rank']=a

            b=((rating[i].text).strip())
            dict['Movie_rating']=b

            c=((Movie_name[i].text).strip())

            dict['Movie_name']=c

            d=((reviews[i].text).strip()) 
            
            dict['Movie_reviews']=d
            
            e=Urls[i]['href']
            movie_url='https://www.rottentomatoes.com/'+ e
            dict['Movie_url']=movie_url
            Top_Movies.append(dict)

            i+=1

    file=open('Task_1.json','w')
    # for data in Top_Movies:
    json.dump(Top_Movies,file,indent=4)

Scrap_Top_Movies()