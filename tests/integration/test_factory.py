""" This module contains tests related to factory function """

import os

from app import create_app


def test_without_config():
    """
    GIVEN the create_app() factory function
    WHEN an app created with empty config
    THEN check test environment execution
    """

    config = {}
    assert not create_app(config).testing


def test_with_test_config_testing():
    """
    GIVEN the create_app() factory function
    WHEN an app created with config for testing environment
    THEN check test environment execution
    """

    config = {
        'TESTING': True,
        'DEBUG': True,
        'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL')
    }
    app = create_app(config)
    assert app.testing
    assert app.debug
    assert app.config.get('SQLALCHEMY_DATABASE_URI') == os.environ.get('DATABASE_URL')


def test_with_development_config():
    """
    GIVEN the create_app() factory function
    WHEN an app created with config for development environment
    THEN check test environment execution
    """

    config = {
        'FLASK_ENV': 'development',
        'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL')
    }
    app = create_app(config)
    assert not app.testing
    assert app.debug
    assert app.config.get('JWT_BLACKLIST_ENABLED') == True
    assert app.config.get('JWT_BLACKLIST_TOKEN_CHECKS') == ['access', 'refresh']
    assert app.config.get('SQLALCHEMY_TRACK_MODIFICATIONS') == False
    assert app.config.get('SECRET_KEY') == 'dev'
    assert app.config.get('JWT_SECRET_KEY') == 'dev'
    assert app.config.get('SQLALCHEMY_DATABASE_URI') == os.environ.get('DATABASE_URL')

def test_with_staging_config():
    """
    GIVEN the create_app() factory function
    WHEN an app created with config for production environment
    THEN check test environment execution
    """

    config = {
        'FLASK_ENV': 'staging',
        'DEBUG': False,
        'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL')
    }
    app = create_app(config)
    from app.config import Staging
    assert not app.testing
    assert not app.debug
    assert app.config.get('JWT_BLACKLIST_ENABLED') == True
    assert app.config.get('JWT_BLACKLIST_TOKEN_CHECKS') == ['access', 'refresh']
    assert app.config.get('SQLALCHEMY_TRACK_MODIFICATIONS') == False
    assert app.config.get('SECRET_KEY') == Staging.SECRET_KEY
    assert app.config.get('JWT_SECRET_KEY') == Staging.JWT_SECRET_KEY
    assert app.config.get('SQLALCHEMY_DATABASE_URI') == os.environ.get('DATABASE_URL')

def test_with_production_config():
    """
    GIVEN the create_app() factory function
    WHEN an app created with config for production environment
    THEN check test environment execution
    """

    config = {
        'FLASK_ENV': 'production',
        'DEBUG': False,
        'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL')
    }
    app = create_app(config)
    from app.config import Production
    assert not app.testing
    assert not app.debug
    assert app.config.get('JWT_BLACKLIST_ENABLED') == True
    assert app.config.get('JWT_BLACKLIST_TOKEN_CHECKS') == ['access', 'refresh']
    assert app.config.get('SQLALCHEMY_TRACK_MODIFICATIONS') == False
    assert app.config.get('SECRET_KEY') == Production.SECRET_KEY
    assert app.config.get('JWT_SECRET_KEY') == Production.JWT_SECRET_KEY
    assert app.config.get('SQLALCHEMY_DATABASE_URI') == os.environ.get('DATABASE_URL')
