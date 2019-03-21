from datetime import datetime

users = []
emails = [{"inbox": []}]


class Emails:
    """class to manipulate emails and users."""

    def __init__(self):
        self.users = users
        self.emails = emails


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

    def send_email(self, subject, message, status, sender_id):
        """add new user."""
        user = {
            "email_id":  len(self.users)+1,
            "createdOn": str(datetime.now()),
            "subject": subject,
            "message": message,
            "status": status,
            "sender_id": sender_id
        }
        self.emails[0]['inbox'].append(user)
        return user


    def search_user_by_email(self, email, password):
        """Search for specific user."""
        search = [
            item for item in self.users if item['email'] == email if item['password'] == password]
        return search    


    def get_all_received_emails(self, email):
        user = self.look_user_by_email(email)
        if user:
            return self.emails[0]['inbox']
        


    def search_user_by_id(self, id):
        """Search for specific user."""
        search = [
            item for item in self.users if item['id'] == id]
        return search 


    def look_user_by_email(self, email):
        """Search for specific user."""
        search = [
            item for item in self.users if item['email'] == email]
        return search 


    def get_all_users(self):
            return self.users


        

