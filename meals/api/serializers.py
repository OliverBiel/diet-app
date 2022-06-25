from rest_framework.serializers import ModelSerializer
from drf_writable_nested import WritableNestedModelSerializer
from servings.api.serializers import ServingSerializer
from meals.models import Meal


class MealSerializer(WritableNestedModelSerializer, ModelSerializer):
    foods = ServingSerializer(many=True)

    class Meta:
        model = Meal
        fields = ['name', "foods"]