from city import City


class Cities:
    def __init__(self):
        self.cities = []

    def add(self, city):
        if not any(c.cityId == city.cityId for c in self.cities):
            self.cities.append(city)
        else:
            raise Exception("City with such Id exists already")

    def delete(self, city_id):
        for city in self.cities:
            if str(city.cityId) == city_id:
                self.cities.remove(city)
                return

    def delete_country(self, country_name):
        self.cities = [city for city in self.cities if city.country != country_name]

    def update(self, city_id, new_name,new_country,new_population):
        for city in self.cities:
            if str(city.cityId)== city_id:
                if new_name:
                    city.name = new_name
                if new_population:
                    city.population = new_population
                if new_country:
                    city.country = new_country


    def millionaire_cities(self):
        return list(filter(lambda x: x.population > 1000000, self.cities))

    def exists(self, id):
        for city in self.cities:
            if str(city.cityId) == id:
                return True
        return False

    def __str__(self):
        return "\n\n".join(str(city) for city in self.cities)