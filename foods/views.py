from rest_framework import mixins, viewsets

from foods.models import FoodCategory
from foods.serializers import FoodListSerializer


class FoodListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.all().order_by('id')
        queryset = (
            queryset.prefetch_related('food')
            .filter(food__is_publish=True)
            .distinct()
        )
        return queryset
