from rest_framework.serializers import ModelSerializer
from servings.api.serializers import ServingSerializer
from meals.models import Meal


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ['name', "foods"]