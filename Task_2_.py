import json
from pprint import pprint
f=open('Task_1.1.json','r')
read_me=f.read()
movies_list=json.loads(read_me)
def group_by_year ():
    New_movie_list=[]
    year_list=[]
    dict_1={}
    c=0
    for movie in movies_list:
        year=movie['year']
        movie_list_2=[]
        # print(movie)
        # print(year,c)
        if year not in year_list:
            year_list.append(year)
            for movie_1 in movies_list:
                # print(movie_1)
                if movie_1['year']==year:
                    movie_list_2.append(movie_1)
                else:
                    pass
        # else:
            # New_movie_list.append(movie_list_2)
            dict_1[year]=movie_list_2
        c+=1
        

    # print(New_movie_list)
    pprint(dict_1)
    return dict_1

# group_by_year()
Movie_dict=group_by_year()

my_file=open('Task_2.json','w')

json.dump(Movie_dict,my_file,indent=4)


# c=0
# for item in dict_1:
#     for item_1 in dict_1[item]:
#         c+=1
#         print(c)