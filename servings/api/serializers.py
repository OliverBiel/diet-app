from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from servings.models import Serving
from foods.api.serializers import FoodSerializer


class ServingSerializer(ModelSerializer):
    foods = serializers.StringRelatedField()

    class Meta:
        model = Serving
        fields = ['id', 'quantity', 'foods']