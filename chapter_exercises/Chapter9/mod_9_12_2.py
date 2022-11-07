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