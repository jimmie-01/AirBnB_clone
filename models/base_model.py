#!/usr/bin/python3
"""
Defines Module for the BaseModel class.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
	"""
		Represents the BaseModel of the HBnB Clone.
	"""

    def __init__(self, *args, **kwargs):
	"""Initialize a new BaseModel.
	
	Args:
		*args: unused.
		**kwargs (dict): (key/value) pairs of attributes.
	"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """Appends current time to updates made to an object.

        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary representation of the Basemodel instance.

        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """Returns the string/readable representation of the BaseModel
	instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
