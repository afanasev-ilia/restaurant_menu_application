from rest_framework import mixins, viewsets

from foods.models import Food, FoodCategory
from foods.serializers import FoodSerializer, FoodListSerializer


class FoodListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
