
@app.route('/api/v1/emails/user/sent/<int:id>', methods=['GET'])
def get_all_user_sent_emails(id):
    """fetch all user emails"""
    return jsonify({"sent-emails": emails.get_user_sent_email(id), "status": 200}), 200