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
