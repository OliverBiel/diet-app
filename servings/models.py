from django.db import models
from foods.models import Food


class Serving(models.Model):
    quantity = models.PositiveIntegerField()
    foods = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity}gr {self.foods.name}'