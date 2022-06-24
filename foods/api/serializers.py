from rest_framework.serializers import ModelSerializer
from foods.models import Food


class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'serving', 'carbo', 'protein', 'fat', 'calories']