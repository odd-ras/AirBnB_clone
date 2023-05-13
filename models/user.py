#!/usr/bin/env python3
"""Module for User model."""
from models.base_model import BaseModel


class User(BaseModel):
    """Define a User object.

    Attributes:
        email (str): Email of user
        password (str): Password of user
        first_name (str): First name of user
        last_name (str): Last name of user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
