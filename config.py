import os


class Config:
    """
    Generate a random string using:
        import os
        import binascii
        binascii.hexlify(os.urandom(24))
    """
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'this_is_for_development_only'
    db_username = os.environ.get('DATABASE_USERNAME')
    db_password = os.environ.get('DATABASE_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or f'mysql+mysqlconnector://{db_username}:{db_password}@bucket/flask-blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
