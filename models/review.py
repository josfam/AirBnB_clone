#!/usr/bin/python3

"""A Review object that represent a review of a person's experience in the
place that they lived in
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review of a person's experience in the place
    that they lived in
    """

    def __init__(self, *args, **kwargs):
        """Creates a Review"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
