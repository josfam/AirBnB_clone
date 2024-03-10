#!/usr/bin/python3

"""A User object that represent a person that is part of the system
(that uses our application)
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user of the AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Creates a User"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
