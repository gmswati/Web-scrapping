import json 
import requests
from bs4 import BeautifulSoup
from pprint import pprint
# from Task_1 import scrap_top_movie 
f=open('Task_1.1.json','r')
read=f.read()
data=json.loads(read)

def scrap_movie_details():
    # for movie in data:
    dict={}
    # link=movie['Movie_url']
    link=data[0]['Movie_url']
    page=requests.get(link)
    prety_page= BeautifulSoup(page.text,'html.parser')
    
    movie_name=prety_page.find('h1').text
    dict['Name']=movie_name
    # print(movie_name)
    div_tag_key=prety_page.find_all('div',class_='meta-label subtle')
    div_tag_value=prety_page.find_all('div',class_='meta-value')
    i=0
    while i<len(div_tag_key):
        key=div_tag_key[i].text.strip().replace(':','')
        value=div_tag_value[i].text.strip().replace('\n','').replace(' ','').split(',')
        if key=='Runtime':
            hr=int(value[0][0])
            if 'm' not in value:
                value=(hr*60)
            else:
                value=(hr*60+int(key[-3:-1]))
            dict[key]=str(value)+' min'

        elif len(value)>1:
            dict[key]=value

        else:
            for item in value:
                dict[key]=item

        # why strip is not working here in value.
        # if value


        i+=1


    pprint(dict)

    
scrap_movie_details()

