#!/usr/bin/python3
"""
This module provides a class that handles file storage
storage. The methods in this class are responsible for
both serialization and deserialization of JSON files
"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """The class `FileStorage` has two private class
    attributes, one that specifies the file path to
    be used for storage and the other which stores
    instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all instances stored in the
        private class attribute, `objects`
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in `__objects` the obj with key (string)
        `<obj class name>.id`
        """
        key_str = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key_str] = obj

    def save(self):
        """Serializes a python dictionary - stored in the
        private class attribute `__objects` to the file
        specified in `__file_path`
        """
        obj_dict = {}

        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
                json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the json file specified in `__file_path`
        and returns/stores it to/in the dictionary specified in
        `__objects`
        """
        file_exists = os.path.exists(FileStorage.__file_path)

        if file_exists:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
                for val in FileStorage.__objects.values():
                    class_name = val["__class__"]
                    if (
                        isinstance(class_name, str) and
                        type(eval(class_name)) == type
                    ):
                        self.new(eval(class_name)(**val))
