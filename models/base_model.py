#!/usr/bin/python3
"""
This module provides the `BaseModel` class _from which
all other classes will inherit. The methods defined
here will be used by all other classes
"""
import uuid
import models
from datetime import datetime, timedelta


class BaseModel:
    """This class defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Converts `datetime` attributes to string representation
        for existing instances, or instantiates a new instance of
        the class
        """
        str_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            # Not a new instance (from a dictionary representation)
            for key, value in kwargs.items():
                if key != "__class__":
                    if (
                        key == "created_at" or
                        key == "updated_at" and
                        isinstance(value, str)
                    ):
                        value = datetime.strptime(value, str_format)
                    setattr(self, key, value)
        else:
            #  A new instance (not from a dictionary representation)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

            # In addition to the above attributes, load the previous attributes
            models.storage.new(self)

    def __str__(self):
        """Returns a meaning string representation of the istance
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """Changes the `updated_at` time and then saves
        the instance to `storage` from the `FileStorage` module
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        `__dict__` of the instance, and adds a keys/value pair
        labelling the instance with the class name
        """
        updated_dict = {}

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                updated_dict[key] = value.isoformat()
            else:
                updated_dict[key] = value

        updated_dict['__class__'] = self.__class__.__name__

        return updated_dict
