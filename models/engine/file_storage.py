#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary."""
        # TODO: should this be a copy()?
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        # TODO: should these be more precise specifiers?
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialzes __objects to JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)
    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict
    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel


        classes = {"BaseModel": BaseModel,
                   }
        return classes 
    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
