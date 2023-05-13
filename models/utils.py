#!/usr/bin/env python3
"""Module for listing available models."""
from models.base_model import BaseModel
from models.user import User

models = {
    "BaseModel": BaseModel,
    "User": User
}
