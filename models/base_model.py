#!/usr/bin/python3

"""A BaseModel class that will be inherited by other classes in this project"""

import uuid
from datetime import datetime as dt
from . import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Create a Base with a unique id, and info about when the object was
        first created, and last updated
        """
        if kwargs and len(kwargs):
            attrs = self.__dict__
            attrs.update(**kwargs)
            # turn created and updated times to normal datetime from iso
            attrs['updated_at'] = dt.fromisoformat(attrs['updated_at'])
            attrs['created_at'] = dt.fromisoformat(attrs['created_at'])
            try:
                # delete the __class__ key from this instance
                del attrs['__class__']
            except KeyError:
                pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            # may differ from creation slightly
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """Non-canonical, human-readable version of this `Base` object"""
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates the public instance attribute `updated_at` with the current
        datetime
        """
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance, and an additional __class__ key.
        Creation and updated times are turned to iso format.
        """
        attrs = {}
        for k, v in self.__dict__.items():  # do not affect the original dict
            attrs.update({k: v})

        class_name = type(self).__name__
        attrs.update({'__class__': class_name})
        # change creation and updated times to iso format
        attrs['updated_at'] = attrs['updated_at'].isoformat()
        attrs['created_at'] = attrs['created_at'].isoformat()
        return attrs
