#!/usr/bin/env python3
"""Module for definition of City model."""
from models.base_model import BaseModel


class City(BaseModel):
    """Define City model instance.

    Attributes:
        name (str): Name of City
        state_id (str): Id of corresponding state
    """

    name = ""
    state_id = ""
