#!/usr/bin/python3
"""Module for FileStorage class"""
import json
import os.path


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __object = {}

    def reload(self):
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            object_dict = json.load(f)
            object_dict = {k: self.classes()[v["__class__"]](**v)
                           for k, v in object_dict.items()}
            FileStorage.__objects = object_dict
