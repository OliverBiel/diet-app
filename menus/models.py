from django.db import models
from meals.models import Meal


class Menu(models.Model):
    name = models.CharField(max_length=200)
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return self.name