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