#!/usr/bin/python3
"""Serializates instances to a JSON file
 and deserializates JSON files to instances
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializates instances to a JSON file
    and deserializates JSON files to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the object in the objects dictionary"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """Serializates objects to JSON file"""
        new_dict = {}
        with open(FileStorage.__file_path, mode="w",
                  encoding="utf-8") as json_file:
            for key in FileStorage.__objects:
                new_dict[key] = (FileStorage.__objects[key]).to_dict()
            json.dump(new_dict, json_file)

    def reload(self):
        """Deserializes JSON file to objects dictionary"""
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as json_file:
                obj_dict = json.load(json_file)
                for key in obj_dict:
                    cls = obj_dict[key].get("__class__")
                    new_obj = exec(cls+"()")
                    self.new(new_obj)
        except:
            pass
