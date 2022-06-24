from rest_framework.viewsets import ModelViewSet
from meals.api.serializers import MealSerializer
from meals.models import Meal


class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer