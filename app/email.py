
from datetime import datetime

users = []
emails = []


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
      
    def send_email(self, subject, message, status, sender_id, receiver_id):
        """add new email."""
        email = {
            "email_id":  len(self.emails)+1,
            "createdOn": str(datetime.now()),
            "subject": subject,
            "message": message,
            "status": status,
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "read": False
        }
        self.emails.append(email)
        return email

    def get_user_email(self, user_id):
        """get user email."""
        emails = [item for item in self.emails if item['receiver_id'] == user_id]
        print(emails)
        return emails


    def delete_user_email(self, id):
        search = self.get_user_email(id)
        if search:
            self.emails.remove(search[0])
            return search
        return "email does not exist"    
        
    def get_user_sent_email(self, user_id):
        """get user email."""
        emails = [item for item in self.emails if item['sender_id'] == user_id]
        return emails
    

    def get_user_unread_email(self, user_id, read):
        """get user email."""
        emails = [item for item in self.emails if item['receiver_id'] == user_id if item['read'] == False]
        return emails

    def search_for_email(self, receiver_id):
        email = [
            item for item in self.emails if item['receiver_id'] == reciever_id]
        return email


    def get_specific_user_email(self, id, email_id):
        email = [email for email in self.emails if email['sender_id'] == id or email['email_id'] == email_id]
        return email

    def search_user_by_email(self, email, password):
        """Search for specific user."""
        search = [
            item for item in self.users if item['email'] == email if item['password'] == password]
        return search
  
    def search_user_by_id(self, id):
        """Search for specific user."""
        search = [
            item for item in self.users if item['id'] == id]
        return search 