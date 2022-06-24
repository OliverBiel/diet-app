from rest_framework.serializers import ModelSerializer
from foods.api.serializers import FoodSerializer
from meals.models import Meal


class MealSerializer(ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        model = Meal
        fiels = ['name', 'foods']