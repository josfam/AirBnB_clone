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
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(objs_dict, f)

    def reload(self):
        """Deserializes the JSON file and stores the result in __objects, only
        if the json file (__file_path) exists. There is no effect at all if the
        file does not exist
        """
        json_file = FileStorage.__file_path
        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
        else:
            # do nothing
            pass
