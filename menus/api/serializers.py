from rest_framework.serializers import ModelSerializer
from meals.api.serializers import MealSerializer
from menus.models import Menu
from drf_writable_nested import WritableNestedModelSerializer


class MenuSerializer(WritableNestedModelSerializer, ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = Menu
        fields = ['name', 'meals']