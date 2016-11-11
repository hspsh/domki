from app.models.mixins import Premises
from django.db import models


class Apartment(Premises):
    """
    Apartment model
    """
    floor = models.PositiveIntegerField(blank=False)
    #floors_in_building = models.PositiveIntegerField(blank=False)
