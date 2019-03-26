
users = []


class User:
    """class to manipulate emails and users."""

    def __init__(self):
        self.users = users

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

    def search_user_by_email(self, email, password):
        """Search for specific user."""
        search = [
            item for item in self.users
            if item['email'] == email if item['password'] == password]
        return search

    def search_user_by_id(self, id):
        """Search for specific user."""
        search = [
            item for item in self.users if item['id'] == id]
        return search
