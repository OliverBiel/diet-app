from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from servings.api.serializers import ServingSerializer
from meals.models import Meal


class MealSerializer(ModelSerializer):
    foods = ServingSerializer(many=True)

    class Meta:
        model = Meal
        fields = ['name', "foods"]