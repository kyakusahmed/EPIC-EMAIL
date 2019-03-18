from datetime import datetime

users = []
emails = []


class Emails:
    """class to manipulate emails and users."""

    def __init__(self):
        self.users = users
        self.emails = emails

  
    def search_user_by_email(self, email):
        """Search for specific user."""
        search = [
            item for item in self.users if item['email'] == email]
        return search    

        
    def add_new_user(self, email, firstname, lastname, password):
        """add new user."""
        user = {
            "id":  len(self.users)+1,
            "email": email,
            "firstname": firstname,
            "lastname": lastname,
            "password": password
        }
        self.users.append(user)
        return user
    

