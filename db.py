#!/usr/bin/python3

import pymysql
import city

class Connection:
    credentials = ("localhost","root","mysql1234","PyCity")
   
    def __init__(self):
        self.db = pymysql.connect(*Connection.credentials)

    def __del__(self):
        self.db.close()
        

    def getAllCities(self):

        query_str = "SELECT code, city FROM PyCity.City;"
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

        try:
            self.cursor.execute(query_str)
        except:
            print("some error occurred... could not read cities from database\n")
            return

        if self.cursor.rowcount == 0:
            print("no cities found\n")
            return

        rows =  self.cursor.fetchall()
        for row in rows:
            print(row["code"] + " " + row["city"])
        
        self.cursor.close()
        
    # read a city record    
    def getCity(self, code):

        city_dic = {}
        query_str = "SELECT * FROM PyCity.City WHERE code ='" + str(code) + "';"
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

        try :
            self.cursor.execute(query_str)
        except:
            print("some error occurred... could not read city from database\n")
            return 
        
        if self.cursor.rowcount == 0:
            print("no code " + code + " found\n")
            return 

        rows =  self.cursor.fetchall()
        for row in rows:
            if row["code"]:
                city_dic['code'] = str(row["code"])
            if row["city"]:
                city_dic['city'] = str(row["city"])
                print("city: " + city_dic["city"])
            if row["population"]:
                city_dic['population'] = int(row["population"])
                print ("population: " + str(city_dic["population"]))
            if row["country"]:
                city_dic['country'] = str(row["country"])
                print("country: " + city_dic["country"])
        
        self.cursor.close()
        return city_dic
        
    # add entry to db
    def addCity(self, cities):
        code = input("insert city code: ")
        name = input("insert city name: ")
        country = input("insert country: ")
        population = int(0)
        while population == 0:
            try:
                population = int(input("insert population: "))
            except:
                print("please insert a valid number")
                
        query_str = "INSERT INTO City (code, city, population, country) VALUES ('"
        query_str += code
        query_str += "', '"
        query_str += name
        query_str += "', "
        query_str += str(population)
        query_str += ", '"
        query_str += country
        query_str += "') ON DUPLICATE KEY UPDATE city = '"
        query_str += name + "', population = " + str(population) + ", country = '" + country + "';"

        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(query_str)
            self.db.commit()
            print("city correctly added to database\n")
        except:
            print("some error occurred.... Try again!\n")
            return

        new_city = city.City(code, name, population, country)
        if self.cursor.rowcount == 1:
            pass
        else:
            for city_ in cities:
                if city_.getCode() == str(code):
                    cities.remove(city_)
                    break

        cities.append(new_city)
        self.cursor.close()
        
        
    # delete an entry using city code
    def deleteCity(self, cities):
        code = input("insert city code: ")
        query_str = "DELETE FROM City WHERE code = '" + str(code) + "';"

        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(query_str)
            self.db.commit()

            if self.cursor.rowcount > 0:
                print("city correctly deleted from database... delete from memory\n")

                for city_ in cities:
                    if city_.getCode() == str(code):
                        cities.remove(city_)
                        break
            else:
                print("city not found\n")
        except:
            print("some error occurred... could not commit changes. Try again!\n")
            
        self.cursor.close()    

        
        
