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


class FoodModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.food_category = FoodCategory.objects.create(
            name_ru='Название тестовой категории',
        )
        cls.food = Food.objects.create(
            category=cls.food_category,
            code=100,
            name_ru='Test food 1',
            cost=10.00
            )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        food = FoodModelTest.food
        field_verboses = {
            'category': 'Раздел меню',
            'is_vegan': 'Вегетарианское меню',
            'is_special': 'Специальное предложение',
            'code': 'Код поставщика',
            'internal_code': 'Код в приложении',
            'name_ru': 'Название на русском',
            'description_ru': 'Описание на русском',
            'description_en': 'Описание на английском',
            'description_ch': 'Описание на китайском',
            'cost': 'Цена',
            'is_publish': 'Опубликовано',
            'additional': 'Дополнительные товары',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    food._meta.get_field(field).verbose_name,
                    expected_value,
                )

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        food = FoodModelTest.food
        field_help_texts = {
            'category': 'Укажите название на русском',
            'is_vegan': 'Укажите название на английском',
            'is_special': 'Укажите название на китайском',
            'code': 'Укажите название на русском',
            'internal_code': 'Укажите название на английском',
            'name_en': 'Укажите название на английском',
            'description_ru': 'Укажите название на китайском',
            'description_en': 'Укажите название на русском',
            'description_ch': 'Укажите название на английском',
            'cost': 'Укажите название на китайском',
            'is_publish': 'Укажите название на русском',
            'additional': 'Укажите название на английском',
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    food._meta.get_field(field).help_text,
                    expected_value,
                )
