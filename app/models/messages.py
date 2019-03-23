from datetime import datetime

users = []
messages = []


class Messages:
    """class to manipulate messages."""

    def __init__(self):
        self.users = users
        self.messages = messages

    def send_message(self, subject, message, status, sender_id, receiver_id, read):
        """add new message."""
        message = {
            "message_id":  len(self.messages)+1,
            "createdOn": str(datetime.now()),
            "subject": subject,
            "message": message,
            "status": status,
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "read": False
        }
        self.messages.append(message)
        return message

    def get_user_message(self, status, read):
        """get user message."""
        for item in self.messages:
            if item['status'] == 'read':
                if item['read'] == False:
                    return item
    
    def search_user_by_id(self, id):
        """Search for specific user."""
        search = [
            item for item in self.users if item['id'] == id]
        return search

    def delete_user_message(self, id):
        search_message = self.search_user_by_id(id)
        if search_message:
            self.messages.remove(search_message[0])
            return search_message
        return "message does not exist"

    def get_user_sent_message(self, status):
        """get user message."""
        messages = [item for item in self.messages if item['status'] == 'sent']
        return messages

    def get_user_unread_message(self, status, read):
        """get user message."""
        messages = [item for item in self.messages
        if item['status'] == 'read' if item['read'] == False]
        return messages

    def get_specific_user_message(self, id, email_id):
        message = [
            message for message in self.messages
            if message['sender_id'] == id or message['email_id'] == email_id]
        return message