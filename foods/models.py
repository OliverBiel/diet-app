from unicodedata import name
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=250)
    portion = models.PositiveIntegerField()     #Porção da comida necessariamente em gramas, assim como todos os macros.
    carbo = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()

    def __str__(self):
        return self.name