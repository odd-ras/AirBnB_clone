#!/usr/bin/env python3
"""Module for definition of Amenity model."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define Amenity model instance.

    Attributes:
        name (str): Name of Amenity
    """

    name = ""
