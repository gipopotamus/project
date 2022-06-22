from django.db import models


# Create your models here.
class Goat(models.Model):
    category = models.CharField(max_length=255)
    is_steep = bool()
    img = models.URLField()

    def __str__(self):
        return id(self)


