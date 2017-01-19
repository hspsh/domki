from django.db import models

# Create your models here.
class Apartment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def publish(self):
        self.save()