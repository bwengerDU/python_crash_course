#11-1 create function to provide city, country formatted name and to test it. Work done in city_functions.py and test_cities.py
from city_functions import formatted_city_name

print("Enter 'quit' at any time to quit.")
while True:
    city = input("\nPlease provide a city name: ")
    if city == 'quit':
        break
    country = input("\nPlease provide the country the city is in: ")
    if country == 'quit':
        break

    formatted_name = formatted_city_name(city, country)
    print(f"Neatly formatted city name: {formatted_name}")

#11-3 

class Employee ():
    """Write class for an employee"""
    def __init__(self, first_name, last_name, salary):
        """Initialize employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """method to give $5k raise to salary amount"""
        self.salary += amount

