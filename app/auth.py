from functools import wraps
from flask import request, jsonify

SECRET_KEY = "personalkey"


def authenticate_request(f):
    @wraps(f)
    def decorted_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token != SECRET_KEY:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)

    return decorted_function
