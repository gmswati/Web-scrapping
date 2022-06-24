import json
from pprint import pprint 
# import 

file=open('Task_5_Movie_details.json','r')
read_file=file.read()
Details=json.loads(read_file)

i=0
Language_list=[]
while i<len(Details):
    if i%2!=0:
        if type(Details[i]["Original Language"])==list:
            for lang in Details[i]["Original Language"]:
                if lang not in Language_list:
                    Language_list.append(lang)
        else:
            lang=Details[i]["Original Language"]
            if lang not in Language_list:
                    Language_list.append(lang)
    i+=1
print(Language_list)

Language_dict={}
for language in Language_list:
    i=0
    No_of_movies=0
    while i<len(Details):
        if i%2!=0:
            if type(Details[i]["Original Language"])==list:
                for lang in Details[i]["Original Language"]:
                    if language==lang:
                        No_of_movies+=1
            else:
                lang=Details[i]["Original Language"]
                if language==lang:
                    No_of_movies+=1
        i+=1
    
    Language_dict[language]=No_of_movies

my_file=open('Task_6_analyse_movies_language.json','w')
# info=my_file.write()
json.dump(Language_dict,my_file,indent=4)
print(Language_dict)

