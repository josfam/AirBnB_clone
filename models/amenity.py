#!/usr/bin/python3

"""An Amenity object that represents an amenity (something that makes living
in a particular location pleasant/comfortable) of a location
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents the Amenity that a particular location comes with"""

    def __init__(self, *args, **kwargs):
        """Creates an Amenity"""
        self.name = ""
        super().__init__(*args, **kwargs)
