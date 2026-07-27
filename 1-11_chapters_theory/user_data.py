# 9.12


class User:
    """User model"""

    def __init__(self, first_name, last_name, age, country, languages):
        """User's information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.languages = languages
        self.login_attempts = 0

    def describe_user(self):
        """Prints user's description."""
        print(
            f"USERS INFORMATION:\n\tFirst name: {self.first_name.title()}\n\tLast name: {self.last_name.title()}\n\tAge: {self.age}\n\tCountry: {self.country.title()}\n\tLanguages: {self.languages}\n"
        )

    def greet_user(self):
        """Personalized greeting the user."""
        print(f"Hi {self.first_name.title()}!\n")

    def increment_login_attempts(self):
        """Counting login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reseting login attempts count to zero."""
        self.login_attempts = 0




class Privileges:
    """Simple privileges model."""

    def __init__(self):
        """Initialize privileges."""
        self.privileges = ['can add post', 'can delete post', 'can bar user']

    def show_privileges(self):
        """Shows all the privileges admin has."""
        print(f"Admin's privileges:\n\t{'\n\t'.join(self.privileges)}")




class Admin(User):
    """Simple subclass of User superclass."""

    def __init__(self, first_name, last_name, age, country, languages):
        """Initialize admin's properties."""
        super().__init__(first_name, last_name, age, country, languages)
        self.privileges = Privileges()
