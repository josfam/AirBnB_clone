#!/usr/bin/python3

"""A City object that represents a city (in the geographical sense), that a
particular location is in
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents the City (in the geographical sense) that a particular
    location is in
    """

    def __init__(self, *args, **kwargs):
        """Creates a City"""
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
