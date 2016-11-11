import uuid
from django.db import models


class Simple(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField('Nazwa', max_length=64)

    class Meta:
        abstract = True


class Premises(Simple):
    rooms = models.PositiveSmallIntegerField('Pokoje')

    class Meta:
        abstract = True
