from django.test import TestCase

from foods.models import FoodCategory, Food
from foods.views import FoodListViewSet


class FoodListViewSetTest(TestCase):
    def setUp(self):
        self.category_without_food = FoodCategory.objects.create(
            name_ru='Тестовая категория без блюд'
        )
        self.category_without_published_food = FoodCategory.objects.create(
            name_ru='Тестовая категория без опубликованных блюд'
        )
        self.category_with_published_food = FoodCategory.objects.create(
            name_ru='Тестовая категория с опубликованными блюдами'
        )
        self.published_food = Food.objects.create(
            name_ru='Опубликованное блюдо',
            code=123,
            cost=1234,
            is_publish=True,
            category=self.category_with_published_food,
        )
        self.unpublished_food = Food.objects.create(
            name_ru='Неопубликованное блюдо',
            code=1234,
            cost=1234,
            is_publish=False,
            category=self.category_without_published_food,
        )
        self.unpublished_food_in_category_with_published_food = (
            Food.objects.create(
                name_ru='Неапубликованное блюдо в категории с опубликованными блюдами',
                code=12345,
                cost=12345,
                is_publish=False,
                category=self.category_with_published_food,
            )
        )

    def test_correct_queryset(self):
        view = FoodListViewSet()
        queryset = view.get_queryset()
        self.assertNotIn(self.category_without_food, queryset)
        self.assertNotIn(self.category_without_published_food, queryset)
        self.assertIn(self.category_with_published_food, queryset)
        self.assertNotIn(
            self.unpublished_food_in_category_with_published_food, queryset
        )
        self.assertNotIn(self.unpublished_food, queryset)
        self.assertEqual(queryset.first(), self.published_food.category)
