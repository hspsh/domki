from django.db import models


class Simple(models.Model):
    name = models.CharField('Nazwa', max_length=64)

    class Meta:
        abstract = True
