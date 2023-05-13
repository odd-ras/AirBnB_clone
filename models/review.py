#!/usr/bin/env python3
"""Module for Review model."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define a Review model.

    Attributes:
        place_id (str): Id of review place
        user_id (str): Id of reviewer
        text (str): Review text
    """

    place_id = ""
    user_id = ""
    text = ""
