@app.route('/api/v1/emails/user/unread/<int:id>', methods=['GET'])
def get_all_user_unread_emails(id):
    """fetch all user unread emails"""
    return jsonify({"unread-emails": emails.get_user_unread_email(id, 'read'), "status": 200}), 200


