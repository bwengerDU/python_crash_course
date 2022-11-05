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
