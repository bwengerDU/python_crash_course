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