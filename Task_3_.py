import json
from pprint import pprint

f=open('Task_2.json','r')

read_file=f.read()
movies_list_by_year=json.loads(read_file)

def group_by_decade():
    list_of_years=[]
    Movie_dict={}
    for year in movies_list_by_year:

        list_of_years.append(int(year))
    # print(list_of_years)
    a=sorted(list_of_years)
    print(a)
    decade_list=[]
    for year in a:
        rem=year%10
        starting_year=year-rem
        if starting_year not in decade_list:
            decade_list.append(starting_year)
    
    for starting_year in decade_list:
        list_1=[]
        final_year=starting_year+10-1
        for year_1 in movies_list_by_year:
            year_2=int(year_1)
            if year_2>=starting_year and year_2<=final_year:
                list_1.append(movies_list_by_year[year_1])
        Movie_dict[starting_year]=list_1
    pprint(Movie_dict)



        

group_by_decade()




































        # for year in :
        # if int(year)>=1920 and int(year) <= 1929:

        #     movie_dict[1920]=movies_list_by_year[year]

        # elif int(year)>=1930 and int(year) <= 1939:
        #     movie_dict[1930]=movies_list_by_year[year]
        
        # elif int(year)>=1940 and int(year) <= 1949:
        #     movie_dict[1940]=movies_list_by_year[year]

        # elif int(year)>=1950 and int(year) <= 1959:
        #     movie_dict[1950]=movies_list_by_year[year]

        # elif int(year)>=1960 and int(year) <= 1969:
        #     movie_dict[1960]=movies_list_by_year[year]

        # elif int(year)>=1970 and int(year) <= 1979:
        #     movie_dict[1970]=movies_list_by_year[year]

        # elif int(year)>=1980 and int(year) <= 1989:
        #     movie_dict[1980]=movies_list_by_year[year]

        # elif int(year)>=1990 and int(year) <= 1999:
        #     movie_dict[1990]=movies_list_by_year[year]

        # elif int(year)>=2000 and int(year) <= 2009:
        #     movie_dict[2000]=movies_list_by_year[year]

        # elif int(year)>=2010 and int(year) <= 2019:
        #     movie_dict[2010]=movies_list_by_year[year]

        # elif int(year)>=2020 and int(year) <= 2029:
        #     movie_dict[2020]=movies_list_by_year[year]




