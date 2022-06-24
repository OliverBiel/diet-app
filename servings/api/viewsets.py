from rest_framework.viewsets import ModelViewSet
from servings.api.serializers import ServingSerializer
from servings.models import Serving


class ServingViewSet(ModelViewSet):
    queryset = Serving.objects.all()
    serializer_class = ServingSerializer