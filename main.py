#!/usr/bin/python3

import sys
import db
import city

def welcomeMessage():
    print("\nWELCOME TO PyCity\n")


def menuOptions():
    print("\n**************************")
    print("press 1 to look for a city")
    print("press 2 to add a city")
    print("press 3 to delete a city")
    print("press 4 to print mem size")
    print("press 5 to list all cities in db")
    print("press 0 to exit")
    print("**************************\n")
    return input("enter your option\n")



def getCity(db_connector, cities):

    code = input("insert city code: ")
    city_dic = {}
    for city_ in cities:
        if city_.getCode() == str(code):
            city_dic = city_
            break

    if bool(city_dic) == True:
        print("\nfound in memory\n")
        print("code: " + city_.getCode())
        print("city: " + city_.getName())
        print("population: " + city_.getPopulation())
        print("country: " + city_.getCountry())        
    else:
        print("\nnot found in memory... try in db\n")
        city_dic = db_connector.getCity(code)

        if bool(city_dic) == True:
            city_code = city_dic.get("code", "")
            city_name = city_dic.get("city", "")
            city_pop = city_dic.get("population", "")
            city_country = city_dic.get("country","")
            new_city = city.City(city_code, city_name, city_pop, city_country)
            cities.append(new_city)

            
if __name__ == "__main__":

    welcomeMessage()
    db_connector = db.Connection()
    cities = []
    
    my_option = int(1)
    while my_option != 0:

        try:
            my_option = int(menuOptions())
        except:
            print("invalid option... please enter valid option")
            continue
                
        print("you selected option " + str(my_option) + "\n")
        if my_option == 1:
            getCity(db_connector,cities)            
        elif my_option == 2:
            db_connector.addCity(cities)
        elif my_option == 3:
            db_connector.deleteCity(cities)
        elif my_option == 4:
            print("list size currently saved in memory: " + str(len(cities)))
        elif my_option == 5:
            db_connector.getAllCities()
        elif my_option == 0:
            break
        else:
            print("invalid option... please enter valid option")

    print("Goodbye...")
    



