from django.db import models
from servings.models import Serving


class Meal(models.Model):
    name = models.CharField(max_length=250)
    foods = models.ManyToManyField(Serving)

    def __str__(self):
        return self.name