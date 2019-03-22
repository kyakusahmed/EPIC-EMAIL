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
