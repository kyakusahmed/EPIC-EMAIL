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
        messages = [item for item in self.messages
        if item['status'] == 'read' if item['read'] == False]
        return messages
    
    def search_user_by_id(self, id):
        """Search for specific user."""
        search_user = [
            item for item in self.users if item['id'] == id]
        return search_user

    def delete_message(self, message_id):
        """delete message."""
        messages = [item for item in self.messages if item['message_id'] == message_id]
        if messages:
            self.messages.remove(messages[0])
            return messages
        return messages

    def get_user_sent_message(self, status):
        """get user message."""
        messages = [item for item in self.messages if item['status'] == 'sent']
        return messages

    def get_user_unread_message(self, status, read):
        """get user message."""
        messages = [item for item in self.messages
        if item['status'] == 'read' if item['read'] == False]
        return messages

    def get_specific_message(self, message_id):
        messages = [item for item in self.messages if item['message_id'] == message_id]
        return messages