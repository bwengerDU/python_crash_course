from mod_9_12_2 import User
from Ch9_TIY import Admin
class Privileges:
    """Privileges class with only one attribute"""
    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
        """list privileges"""
        self.privileges = privileges
    def show_privileges(self):
        """Print out list of privileges for Admin users"""
        print(f"As an admin user, you are able to do the following actions: {self.privileges}.")