from django.test import TestCase
from app.models.apartment import Apartment


class TestApartment(TestCase):
    "Show setup and teardown"

    def setUp(self):
        Apartment.objects.create(name="pierwszy", floor=3, rooms=7)

    def test_apartment(self):
        """Apartment has the same params, as created"""
        obj = Apartment.objects.get(name="pierwszy")
        self.assertEqual(obj.floor, 3)
        self.assertEqual(obj.rooms, 7)
