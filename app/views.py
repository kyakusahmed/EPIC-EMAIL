@app.route('/api/v1/emails/user/delete/<int:id>', methods=['DELETE'])
def delete_user_emails(id):
    """delete user's email"""
    return jsonify({"deleted email": emails.delete_user_email(id), "status": 200}), 200
