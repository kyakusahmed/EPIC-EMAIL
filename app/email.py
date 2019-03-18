from datetime import datetime

users = []
emails = [{"inbox": []}, {"sent": []}, {"drafts": []}]


class Emails:
    """class to manipulate emails and users."""

    def __init__(self):
        self.users = users
        self.emails = emails


    def search_user_by_id(self, id):
        """Search for specific user."""
        search = [
            item for item in self.users if item['id'] == id]
        return search    

    def get_all_recieved_emails_by_user(self, id):
        """view all recieved emails"""
        search = self.search_user_by_id(id)
        if search:
            return self.emails[0]['inbox']
        return "user does not exist"    
        

        
        