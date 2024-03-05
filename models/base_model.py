#!/usr/bin/python3

"""A BaseModel class that will be inherited by other classes in this project"""

import uuid
from datetime import datetime as dt


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """Create a Base with a unique id, and info about when the object was
        first created, and last updated
        """
        self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            # may differ from creation slightly
            self.updated_at = dt.now()

    def __str__(self):
        """Non-canonical, human-readable version of this `Base` object"""
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates the public instance attribute `updated_at` with the current
        datetime
        """
        self.updated_at = dt.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance, and an additional __class__ key.
        Creation and updated times are turned to iso format.
        """
        attrs = self.__dict__
        class_name = type(self).__name__
        attrs.update({'__class__': class_name})
        # change creation and updated times to iso format
        attrs['updated_at'] = attrs['updated_at'].isoformat()
        attrs['created_at'] = attrs['created_at'].isoformat()
        return attrs
