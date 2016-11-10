from app.models.mixins import Simple
from django.db import models


class Apartment(Simple):
    """
    Apartment model
    """
    floor = models.PositiveIntegerField(blank=False)
    #floors_in_building = models.PositiveIntegerField(blank=False)
