#!/usr/bin/python3
"""Module for FileStorage class"""
import json
import os.path


class FileStorage:
    def reload(self):
        """Deserializes json files into objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            object_dict = json.load(f)
            object_dict = {k: self.classes()[v["__class__"]](**v)
                           for k, v in object_dict.items()}
            FileStorage.__objects = object_dict
