#!/usr/bin/python3

"""Serializing objects to JSON, and deserializing a JSON file to
recreate instances
"""

import json
import os


class FileStorage:
    """Serializing and deserializing objects and JSON files respectively"""

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """Returns the private dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        value = obj
        new_dict = {key: value}
        self.all().update(new_dict)

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_file = FileStorage.__file_path
        objs_dict = FileStorage.__objects

        # turn objects to their dictionary representations
        to_save = dict()
        for k, v in objs_dict.items():
            to_save.update({k: v.to_dict()})

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(to_save, f)

    def reload(self):
        """Deserializes the JSON file and stores the result in __objects, only
        if the json file (__file_path) exists. There is no effect at all if the
        file does not exist
        """
        json_file = FileStorage.__file_path
        FileStorage.__objects = dict()
        if os.path.exists(json_file):
            # delayed import of BaseModel to work around circular import error
            from models.base_model import BaseModel
            from models.user import User

            legal_classes = {
                'BaseModel': BaseModel,
                'User': User,
            }
            with open(json_file, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)

                for key, attrs in json_dict.items():
                    # dynamically determine this object's class before creating
                    # it
                    class_type = attrs['__class__']
                    obj = legal_classes[class_type](**attrs)
                    FileStorage.__objects.update({key: obj})
        else:
            # do nothing
            pass
