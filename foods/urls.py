from django.urls import include, path
from rest_framework.routers import DefaultRouter

from foods.apps import FoodsConfig
from foods.views import FoodListViewSet

app_name = FoodsConfig.name

router = DefaultRouter()
router.register(
    'foods',
    FoodListViewSet,
    basename='foods',
)

urlpatterns = [
    path('', include(router.urls)),
]
