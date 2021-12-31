from flaskapp.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

def user_auth(username, password_hash):
        db = get_db()
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        user_dict = {
            'user': user,
            'error': None
        }
        if user is None:
            user_dict['error'] = 'Incorrect username'
        elif not check_password_hash(generate_password_hash(password_hash), password=password_hash):
            user_dict['error'] = 'Incorrect password'
        
        return user_dict