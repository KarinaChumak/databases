from Country import Country


class Countries:
    def __init__(self):
        self.countries = []

    def add(self, country):
        if not any(c.countryName == country.countryName for c in self.countries):
            self.countries.append(country)
        else:
            raise Exception("This country exists already")

    def delete(self, country_name):
        for country in self.countries:
            if country.countryName == country_name:
                self.countries.remove(country)

    def update(self, country_name, new_capital, new_largest, new_currency):
        for country in self.countries:
            if country.countryName == country_name:
                if new_capital:
                    country.capital = new_capital
                if new_largest:
                    country.largestCity = new_largest
                if new_currency:
                    country.currency = new_currency


    def find_three_millionaire_cities(self, millionaire_cities):
        result = []
        for country in self.count_cities(millionaire_cities).keys():
            result.append(self.get_country(country))
        return result

    def get_country(self, name):
        for country in self.countries:
            if country.countryName == name:
                return country

    def count_cities(self, millionaire_cities):
        count_dictionary = {}
        for city in millionaire_cities:
            if city.country in count_dictionary:
                count_dictionary[city.country] += 1
            else:
                count_dictionary[city.country] = 1
        count_dictionary = dict((key, value) for key, value in count_dictionary.items() if value >= 3)
        return count_dictionary

    def exists(self,name):
        for country in self.countries:
            if country.countryName == name:
                return True
        else:
            return False

    def __str__(self):
        return "\n\n".join(str(country) for country in self.countries)