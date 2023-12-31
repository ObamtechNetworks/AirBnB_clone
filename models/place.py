#!/usr/bin/python3

"""this module defines a class place
this class inherits from baseModel
It creates a new place objects
while inheriting all properties of baseModel
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """A blueprint for all place objects
    it inherits all properties from baseModel
    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
