from rest_framework.viewsets import ModelViewSet
from menus.api.serializers import MenuSerializer
from menus.models import Menu


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer