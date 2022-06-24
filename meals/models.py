from django.db import models
from foods.models import Food


class Meal(models.Model):
    name = models.CharField(max_length=250)
    foods = models.ManyToManyField(Food)

    def __str__(self):
        return self.name