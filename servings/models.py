from django.db import models
from foods.models import Food


class Serving(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField()
    foods = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)