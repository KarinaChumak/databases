class Country:
    def __init__(self, countryName, capital, largestCity, currency):
        self.countryName = countryName
        self.capital = capital
        self.largestCity = largestCity
        self.currency = currency

    def __str__(self):
        return "Country: " + self.countryName + "\nCapital: " + self.capital + "\nLargest city: " + self.largestCity +\
               "\nCurrency: " + self.currency

