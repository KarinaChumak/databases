class City:
    def __init__(self, city_id, name, country, population):
        self.cityId = city_id
        self.name = name
        self.country = country
        self.population = population

    def __str__(self):
        return "Id:%s City: %s  Country:%s  Population: %s" %(self.cityId, self.name, self.country, self.population)

