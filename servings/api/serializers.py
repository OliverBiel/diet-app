from rest_framework.serializers import ModelSerializer
from servings.models import Serving
from foods.api.serializers import FoodSerializer


class ServingSerializer(ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        model = Serving
        fields = ['id', 'name','quantity', 'foods']