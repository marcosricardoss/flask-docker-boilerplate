"""This module contains class whose instances will be used to
load the settings according to the running environment. """


import os


class Default():
    """Class containing the default settings for all environments.

    Constants:
        SQLALCHEMY_TRACK_MODIFICATIONS (boolean): signals to get notified
        before and after changes are committed to the database.
    """
    DEBUG = False
    TESTING = False
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Default):
    """Class containing the settings of the production environment .

    It load some values from the environment to be used in the internal Flask config.

    Constants:
        SECRET_KEY (str): The application secret key used to encrypt your cookies.
        SQLALCHEMY_DATABASE_URI (str): URI for the database source.
    """

    SECRET_KEY = b'\xceY\x01\x1e\xc1\x13\x05\xc3\xaa\xfb\xe7\xc5\xe9\x8b\xdaW'
    JWT_SECRET_KEY = b'\xceY\x01\x1e\xc1\x13\x05\xc3\xaa\xfb\xe7\xc5\xe9\x8b\xdaW'    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class Staging(Default):
    """Class containing the settings of the staging environment .

    It load some values from the environment to be used in the internal Flask config.

    Constants:
        SECRET_KEY (str): The application secret key used to encrypt your cookies.
        SQLALCHEMY_DATABASE_URI (str): URI for the database source.
    """

    SECRET_KEY = b'\xacP=\x12\xa6\xa2\x19`\xbcu{\x0b\xe4&H\x8d'
    JWT_SECRET_KEY = b'\xacP=\x12\xa6\xa2\x19`\xbcu{\x0b\xe4&H\x8d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class Development(Default):
    """Class containing the settings of the development environment.

    It uses the dotenv library to load some values from the .env file to environment.
    After that, theses values are load from the environment to be use in the internal Flask config.

    Constants:
        SECRET_KEY (str): The application secret key used to encrypt your cookies.
        SQLALCHEMY_DATABASE_URI (str): URI for the database source.
    """

    DEBUG = True
    SECRET_KEY = 'dev'
    JWT_SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
