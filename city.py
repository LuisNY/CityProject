
class City:

    tot_number = 0
    
    def __init__(self, code, name, population, country):
        self.code = code
        self.name = name
        self.population = population
        self.country = country
        self.__class__.tot_number += 1

    def __eq__(self, other):
        return self.name == other.name
        
    def getName(self):
        return str(self.name)

    def getPopulation(self):
        return str(self.population)

    def getCountry(self):
        return str(self.country)

    def getCode(self):
        return str(self.code)
    
    def getTotNumber():
        return int(City.tot_number)
