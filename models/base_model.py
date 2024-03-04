#!/usr/bin/python3

"""A BaseModel class that will be inherited by other classes in this project"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """Create a Base with a unique id, and info about when the object was
        first created, and last updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()  # will differ from creation slightly

    def __str__(self):
        """Non-canonical, human-readable version of this `Base` object"""
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates the public instance attribute `updated_at` with the current
        datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance, and an additional __class__ key.
        Creation and updated times are turned to iso format.
        """
        self_dict = self.__dict__
        class_name = type(self).__name__
        self_dict.update({'__class__': class_name})
        # change creation and updated times to iso format
        self_dict['updated_at'] = self_dict['updated_at'].isoformat()
        self_dict['created_at'] = self_dict['created_at'].isoformat()
        return self_dict
