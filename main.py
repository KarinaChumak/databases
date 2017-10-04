from Country import Country
from Countries import Countries
from city import City
from Cities import Cities
import sys, os
import pickle
import atexit

# ukraine = Country("Ukraine", "Kyiv", "Kyiv", "hryvna")
# usa = Country("USA", "Washington", "New York", "dollar")
# france = Country("France", "Paris", "Paris","euro")
# germany = Country("Germany", "Berlin", "Berlin", "euro")
#
# cl = Countries()
# cl.add(ukraine)
# cl.add(usa)
# cl.add(france)
# cl.add(germany)
#
# kyiv = City(0,"Kyiv", "Ukraine",3000000)
# donetsk = City(1,"Donetsk", "Ukraine",922137)
# kharkov = City(2,"Kharkov","Ukraine", 1447881)
# boston = City(4,"Boston", "USA", 636479)
# ny = City(3,"New york", "USA", 8550405)
# philadelphia = City(5,"Philadelphia","USA", 1560297)
# la = City(6,"Los Angeles", "USA", 3792621)
# paris = City(7, "Paris", "France", 2249975)
# marceille = City(8, "Marseille", "France", 855393)
# lyon = City(9,"Lyon", "France",500715)
# toulouse= City(10, "Toulouse", "France",458298)
# berlin = City(11,"Berlin","Germany", 3460725)
# hamburg = City(12,"Hamburg", "Germany", 1786448)
# munchen = City(13, "Munchen", "Germany", 1353186)
# cologne = City(14, "Cologne", "Germany", 1007119)
#
# cities = Cities()
# cities.add(kyiv)
# cities.add(donetsk)
# cities.add(kharkov)
# cities.add(philadelphia)
# cities.add(ny)
# cities.add(boston)
# cities.add(la)
# cities.add(paris)
# cities.add(marceille)
# cities.add(lyon)
# cities.add(toulouse)
# cities.add(berlin)
# cities.add(hamburg)
# cities.add(munchen)
# cities.add(cologne)

with open('cities.pickle', 'rb') as f:
    cities = pickle.load(f)


with open('countries.pickle', 'rb') as f:
    countries = pickle.load(f)

menu_actions = {}
help_options = [
   "show",
   "add",
   "delete",
   "modify",
   "filter",
   "exit"

]

def main_menu():

    help()
    choice = input(" >>  ")
    execute_menu(choice)
    return

def help():
   print("Commands:\n")
   for command in help_options:
      print(command)


def execute_menu(choice):

   ch = choice.lower()
   if ch == '':
      menu_actions['main_menu']()
   else:
      try:
         menu_actions[ch]()
      except KeyError:
         print("Invalid selection, please try again.\n")
         menu_actions['main_menu']()
   return

def show():
   print("1.Cities\n2.Countries")
   choice = input(">> ")
   if choice == '1':
      print(cities)
   elif choice == '2':
      print(countries)
   else:
      print("Invalid selection, please try again.\n")
      menu_actions['main_menu']()
   input("Press anything to return")
   menu_actions['main_menu']()
   return


def add():
   print("1.Cities\n2.Countries")
   choice = input(">>")
   if choice == '1':
      add_city()
   elif choice == '2':
      add_country()
   else:
      print("Invalid selection, please try again.\n")
      menu_actions['main_menu']()
   input("Press anything to return")
   menu_actions['main_menu']()
   return

def modify():
   print("1.Cities\n2.Countries")
   choice = input(">>")
   if choice == '1':
      modify_city()
   if choice == '2':
      modify_country()
   else:
      print("Invalid selection, please try again.\n")
      menu_actions['main_menu']()
   input("Press anything to return")
   menu_actions['main_menu']()
   return

def delete():
   print("1.Cities\n2.Countries")
   choice = input(">>")
   if choice == '1':
      delete_city()
   if choice == '2':
      delete_country()
   else:
      print("Invalid selection, please try again.\n")
      menu_actions['main_menu']()
   input("Press anything to return")
   menu_actions['main_menu']()
   return

def delete_city():
   id = input("Select id: ")
   cities.delete(id)
   input("Press anything to return")
   menu_actions['main_menu']()
   return

def delete_country():
   name = input("Select name: ")
   countries.delete(name)
   cities.delete_country(name)
   input("Press anything to return")
   menu_actions['main_menu']()
   return

def modify_city():
   id = input("ID: ")
   name = input("New name: ")
   country = input("New country: ")
   population = input("Updated population: ")
   if cities.exists(id):
      cities.update(id,name, country, population)
   else:
      print("Wrong id")
   input("Press anything to return")
   menu_actions['main_menu']()
   return

def modify_country():
   name = input("Name: ")
   capital = input("New capital: ")
   largest = input("New largest city: ")
   currency = input("New currency: ")
   if countries.exists(name):
      countries.update(name, capital, largest, currency)
   else:
      print("Wrong name")
   input("Press anything to return")
   menu_actions['main_menu']()
   return

def add_city():
   id = input("ID: ")
   name = input("Name: ")
   country = input("Country: ")
   population = input("Population: ")
   if name and country and population and not cities.exists(id):
         new_city = City(id,name,country,population)
         cities.add(new_city)
   else:
      print("Wrong data")
   input("Press anything to return")
   menu_actions['main_menu']()
   return

def add_country():
   name = input("Name: ")
   capital = input("Capital: ")
   largest = input("Largest city: ")
   currency = input("Currency: ")
   if capital and largest and currency and not countries.exists(name):
         new_country= Country(name,capital,largest,currency)
         countries.add(new_country)
   else:
      print("Wrong data")
   input("Press anything to return")
   menu_actions['main_menu']()
   return

def filter():
   for country in countries.find_three_millionaire_cities(cities.millionaire_cities()):
       print(country)
   input("Press anything to return")
   menu_actions['main_menu']()

def exit():
   # with open('cities.pickle', 'wb') as f:
   #    pickle.dump(cities, f)
   # with open('countries.pickle', 'wb') as g:
   #    pickle.dump(countries,g)
   sys.exit()


menu_actions = {
   'main_menu': main_menu,
   'show': show,
   'add': add,
   'delete': delete,
   'filter': filter,
   'modify':modify,
   'exit': exit,
}

if __name__ == "__main__":

   main_menu()
