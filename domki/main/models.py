from django.db import models


# Create your models here.
class Home(models.Models):
    TYPES = (
        (1,"one_room"),
        (2,"flat"),
        (3,"apartment"),
        (4,"house"),
        (5,"place_in_room"),
    )

    city = models.CharField(max_length=10, blank=True)
    street = models.CharField(max_length=10, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    building_number = models.CharField(max_length=10, blank=True)
    apartment_number = models.CharField(max_length=10, blank=True)
    type_of_rent = models.CharField(choices=TYPES, blank=false)

#     equipment
    washing = models.BooleanField(default=False)
    shower = models.BooleanField(default=False)
    bath = models.BooleanField(default=False)
    oven = models.BooleanField(default=False)
    bed = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    freezer = models.BooleanField(default=False)
    dryer = models.BooleanField(default=False)

# equipment ends here
