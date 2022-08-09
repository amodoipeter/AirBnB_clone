#!/usr/bin/python3
"""Module for FileStorage class"""
import json
import os.path


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def reload(self):
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            object_dict = json.load(f)
            object_dict = {k: self.classes()[v["__class__"]](**v)
                           for k, v in object_dict.items()}
            FileStorage.__objects = object_dict
