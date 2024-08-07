from django.test import TestCase

from foods.models import FoodCategory


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
        food_category = FoodCategoryModelTest.food_category
        field_verboses = {
            'name_ru': 'Название на русском',
            'name_en': 'Название на английском',
            'name_ch': 'Название на китайском',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    food_category._meta.get_field(field).verbose_name,
                    expected_value,
                )

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        food_category = FoodCategoryModelTest.food_category
        field_help_texts = {
            'name_ru': 'Укажите название на русском',
            'name_en': 'Укажите название на английском',
            'name_ch': 'Укажите название на китайском',
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    food_category._meta.get_field(field).help_text,
                    expected_value,
                )
