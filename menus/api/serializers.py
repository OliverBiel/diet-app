from rest_framework.serializers import ModelSerializer
from meals.api.serializers import MealSerializer
from menus.models import Menu


class MenuSerializer(ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = Menu
        fields = ['name', 'meals']