#!/usr/bin/python3

"""A State object that represent a state (in the geographical sense), that a
particular location is in
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents the State (in the geographical sense) of a particular
    location
    """

    def __init__(self, *args, **kwargs):
        """Creates a State"""
        self.name = ""
        super().__init__(*args, **kwargs)
