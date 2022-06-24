from rest_framework.viewsets import ModelViewSet
from foods.models import Food
from foods.api.serializers import FoodSerializer


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer