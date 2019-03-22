@app.route('/api/v1/emails/specific-user/<int:id>', methods=['GET'])
def get_specific_user_email(id):
    """get specific user's email"""
    return jsonify({"status": 200, "specific user email": emails.get_specific_user_email(id, 'email_id')})


