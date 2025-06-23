from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

class User:
    def __init__(self, email: str, hashed_password: str):
        self.email = email
        self.hashed_password = hashed_password

class Task:
    def __init__(self, title: str, description: str, status: str, owner_id: str):
        self.title = title
        self.description = description
        self.status = status
        self.owner_id = owner_id 