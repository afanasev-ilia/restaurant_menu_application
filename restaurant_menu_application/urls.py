from django.contrib import admin
from django.urls import include, path

from foods.apps import FoodsConfig

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('foods.urls', namespace=FoodsConfig.name)),
]
