#!/usr/bin/env python3
"""Module for definition of Place model."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Define Place model instance.

    Attributes:
        name (str): Name of Place
        city_id (str): Id of corresponding city
        state_id (str): Id of corresponding state
        user_id (str): Id of corresponding user
        description (str): Description of place
        number_rooms (int): Number of rooms in place
        number_bathrooms (int): Number of bathrooms in place
        max_guest (int): Maximum number of guests for place
        price_by_night (int): Price of place by night
        latitude (float): Latitude of place
        longitude (float): Longitude of place
        amenity_ids (list[str]): List of amenity ids for place
    """

    name = ""
    city_id = ""
    state_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
