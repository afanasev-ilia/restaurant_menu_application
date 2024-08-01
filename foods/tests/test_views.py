from django.test import TestCase

from foods.models import FoodCategory, Food
from foods.views import FoodListViewSet


class FoodListViewSetTest(TestCase):
    def setUp(self):
        self.category_without_food = FoodCategory.objects.create(
            name_ru="Test category without_food"
        )
        self.category_without_published_food = FoodCategory.objects.create(
            name_ru="Test category without published food"
        )
        self.category_with_published_food = FoodCategory.objects.create(
            name_ru="Test category with published food"
        )
        self.published_food = Food.objects.create(
            name_ru="Published Food",
            code=123,
            cost=1234,
            is_publish=True,
            category=self.category_with_published_food,
        )
        self.unpublished_food = Food.objects.create(
            name_ru="Unpublished Food",
            code=1234,
            cost=1234,
            is_publish=False,
            category=self.category_without_published_food,
        )
        self.unpublished_food_in_category_with_published_food = Food.objects.create(
            name_ru="Unpublished Food in category with published food",
            code=12345,
            cost=12345,
            is_publish=False,
            category=self.category_with_published_food,
        )

    def test_correct_queryset(self):
        view = FoodListViewSet()
        queryset = view.get_queryset()
        self.assertNotIn(self.category_without_food, queryset)
        self.assertNotIn(self.category_without_published_food, queryset)
        self.assertIn(self.category_with_published_food, queryset)
        self.assertNotIn(self.unpublished_food_in_category_with_published_food, queryset)
        self.assertNotIn(self.unpublished_food, queryset)
        self.assertEqual(queryset.first(), self.published_food.category)
