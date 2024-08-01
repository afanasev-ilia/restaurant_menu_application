from rest_framework import mixins, viewsets

from foods.models import FoodCategory
from foods.serializers import FoodListSerializer


class FoodListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        return (
            FoodCategory.objects.all()
            .prefetch_related('food')
            .filter(food__is_publish=True)
            .distinct()
            .order_by('id')
        )
