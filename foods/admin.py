from django.contrib import admin

from foods.models import Food, FoodCategory


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'internal_code',
        'code',
        'name_ru',
        'description_ru',
        'description_en',
        'description_ch',
        'is_vegan',
        'is_special',
        'cost',
    )


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name_ru',
        'name_en',
        'name_ch',
        'order_id',
    )
