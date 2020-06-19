"""It contains tests for the Model class from the models.py module"""

import pytest

def test_base_model(session, mocker):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the serialize() and remove_session() methods
    """

    import sqlalchemy
    from app.model.models import Model
    
    mocker.patch('sqlalchemy.inspect')

    model = Model()
    assert model.serialize() == {}   
    model.remove_session()
    sqlalchemy.inspect.assert_called_once()
