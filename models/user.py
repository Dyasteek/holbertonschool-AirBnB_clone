#!/usr/bin/python3

from models.base_model import BaseModel
""" Define the User class """


class User(BaseModel):
    """ User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
