from django.test import TestCase

from foods.models import Food, FoodCategory


class FoodCategoryModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.food_category = FoodCategory.objects.create(
            name_ru='Название тестовой категории',
            name_en='Название на английском тестовой категории',
            name_ch='Название на китайском тестовой категории',
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        task = FoodCategoryModelTest.food_category
        field_verboses = {
            'name_ru': 'Название на русском',
            'name_en': 'Название на английском',
            'name_ch': 'Название на китайском',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)
