from django.db import models
from servings.models import Serving


class Meal(models.Model):
    name = models.CharField(max_length=250)
    foods = models.ManyToManyField(Serving)

    def ShowFoodsName(self):
        foods = [foods.id for foods in self.foods.all()]
        return Serving.objects.filter()

    def __str__(self):
        return self.name
        