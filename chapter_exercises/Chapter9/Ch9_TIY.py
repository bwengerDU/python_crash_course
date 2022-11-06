#9-1
class Restaurant: 
    """Create Class for a Mexican restaurant called Wapos."""
    def __init__(self, restaurant_name, cuisine_type):
        """initialize name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """Print the two attributes"""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} food")
    def open_restaurant(self):
        """Declare that the restaurant is open"""
        print(f"{self.restaurant_name.title()} is now open")
restaurant = Restaurant('wapos', 'mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2
#Create three separate instances and call describe restaurant for each 
birdhouse = Restaurant('birdhouse', 'ramen')
lucilles = Restaurant('lucilles', 'cajun')
echo = Restaurant('echo', 'italian')

birdhouse.describe_restaurant()
lucilles.describe_restaurant()
echo.describe_restaurant()

#9-3
class User:
    """Create user class with several user categories"""
    def __init__(self, first_name, last_name, user_name, user_type,):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_type = user_type

    def describe_user(self):
        """User summary response to command"""
        print(f"{self.first_name.title()} {self.last_name.title()} is a {self.user_type.title()} level user that will appear in the system as {self.user_name}.")
    def greet_user(self):
        """Greeting to user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}! Welcome to the system. Your username is {self.user_name} and your access level is {self.user_type.title()}.")
#Create several instances for different users and print both messages
allen = User('allen', 'murner', 'amurner', 'entry')
miles = User('miles', 'miglia', 'mmiglia', 'intermediate')
lex = User('lex', 'tucky', 'ltucky', 'master')

allen.describe_user()
allen.greet_user()
miles.describe_user()
miles.greet_user()
lex.describe_user()
lex.greet_user()

#9-4
class Restaurant: 
    """Create Class for a Mexican restaurant called Wapos."""
    def __init__(self, restaurant_name, cuisine_type):
        """initialize name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """Print the two attributes"""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} food")
    def open_restaurant(self):
        """Declare that the restaurant is open"""
        print(f"{self.restaurant_name.title()} is now open")
    def set_number_served(self):
        """"attribute counting the number of served patrons"""
        print(f"There has been {self.number_served} customers served.")
    def update_number_served(self, customers):
        """set the number of customers served to a given value"""
        self.number_served = customers
    def increment_number_served(self, customer):
        """Add the given amount to the number of customers served"""
        self.number_served  += customer

restaurant = Restaurant('wapos', 'mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.update_number_served(16)
restaurant.set_number_served()
restaurant.increment_number_served(62)
restaurant.set_number_served() 

#9-5 Adding attibute login_attempts, method called increment_login_attempts, method reset_login_attempts, printing login attempts
class User:
    """Create user class with several user categories"""
    def __init__(self, first_name, last_name, user_name, user_type, login_attempts,):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_type = user_type
        self.login_attempts = 0

    def describe_user(self):
        """User summary response to command"""
        print(f"{self.first_name.title()} {self.last_name.title()} is a {self.user_type.title()} level user that will appear in the system as {self.user_name}.")
    def greet_user(self):
        """Greeting to user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}! Welcome to the system. Your username is {self.user_name} and your access level is {self.user_type.title()}.")
    def increment_login_attempts(self, logins):
        """increment value of login_attempts by 1"""
        self.login_attempts += logins
    def reset_login_attempts(self):
        """resets login_attempts to 0"""
        self.login_attempts = 0
#Create several instances for different users and print both messages
allen = User('allen', 'murner', 'amurner', 'entry', '0')
miles = User('miles', 'miglia', 'mmiglia', 'intermediate', '0')
lex = User('lex', 'tucky', 'ltucky', 'master', '0')

allen.describe_user()
allen.greet_user()
miles.describe_user()
miles.greet_user()
lex.describe_user()
lex.greet_user()

#make instance of user class and call increment_login_attempts(). Show that it is incrementing correctly, then call reset to 0, show that is has reset. 
allen.increment_login_attempts(1)
allen.login_attempts
allen.increment_login_attempts(1)
allen.login_attempts
allen.increment_login_attempts(1)
allen.login_attempts
print(f"Allen has attempted to login {allen.login_attempts} times.")
allen.reset_login_attempts()
allen.login_attempts
print(f"Allen has now attempted to login {allen.login_attempts} times.")

#9-6 Inherit class from Restaurant above. 
class IceCreamStand(Restaurant):
    """New class, adding flavors as an attribute"""
    def __init__(self, restaurant_name, cuisine_type):
        """initial parent class attributes"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'butterscotch', 'strawberry', 'chocolate']
    def list_flavors(self):
        """Print a statement stating the available ice cream flavors"""
        print(f"We have the following ice cream flavors: {self.flavors}.")
#create instance and call method to list ice cream flavors
show_flavors = IceCreamStand('wapos', 'mexican')
show_flavors.list_flavors()

#9-7
class Admin(User):
    """Admin account intaking User class settings, with additional changes unique to Admin users"""
    def __init__(self, first_name, last_name, user_name, user_type, login_attempts):
        """Initialize User attributes and adding Admin attributes"""
        super().__init__(first_name, last_name, user_name, user_type, login_attempts)
#add below instance for 9-8
        self.privileges = Privileges()
#(originally in 9-7, changed for 9-8)        self.privileges = ['can add post', 'can delete post', 'can ban user']
#(originally in 9-7, changed for 9-8)    def show_privileges(self):
#(originally in 9-7, changed for 9-8)        """Print out list of privileges for Admin users"""
#(originally in 9-7, changed for 9-8)        print(f"As an admin user, you are able to do the following actions: {self.privileges}.")
#(originally in 9-7, changed for 9-8)admin_privileges = Admin('cody', 'baggins', 'cbaggins', 'admin', '1')
#(originally in 9-7, changed for 9-8)admin_privileges.show_privileges()

#9-8
class Privileges:
    """Privileges class with only one attribute"""
    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
        """list privileges"""
        self.privileges = privileges
    def show_privileges(self):
        """Print out list of privileges for Admin users"""
        print(f"As an admin user, you are able to do the following actions: {self.privileges}.")
admin_privileges = Admin('cody', 'baggins', 'cbaggins','admin', '1')
admin_privileges.privileges.show_privileges()

#9-9
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

#9-10 Importing the Restaurant class into that program file. Saved as restaurant.py


    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")
    
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()