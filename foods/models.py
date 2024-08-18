from django.db import models
from model_utils.models import TimeStampedModel


class FoodCategory(TimeStampedModel):
    name_ru = models.CharField(
        verbose_name='Название на русском',
        max_length=255,
        unique=True,
        help_text='Укажите название на русском',
    )
    name_en = models.CharField(
        verbose_name='Название на английском',
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        help_text='Укажите название на английском',
    )
    name_ch = models.CharField(
        verbose_name='Название на китайском',
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        help_text='Укажите название на китайском',
    )
    order_id = models.SmallIntegerField(
        default=10,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Раздел меню'
        verbose_name_plural = 'Разделы меню'
        ordering = ('name_ru', 'order_id')


class Food(TimeStampedModel):
    category = models.ForeignKey(
        FoodCategory,
        verbose_name='Раздел меню',
        related_name='food',
        on_delete=models.CASCADE,
        help_text='Укажите раздел меню',
    )

    is_vegan = models.BooleanField(
        verbose_name='Вегетарианское меню',
        default=False,
        help_text='Укажите относится ли блюдо к вегетарианскому меню',
    )
    is_special = models.BooleanField(
        verbose_name='Специальное предложение',
        default=False,
        help_text='Укажите является ли блюдо специальным предложением',
    )

    code = models.IntegerField(
        verbose_name='Код поставщика',
        help_text='Укажите код поставщика',
    )
    internal_code = models.IntegerField(
        verbose_name='Код в приложении',
        unique=True, null=True,
        blank=True,
        help_text='Укажите код в приложении',
    )

    name_ru = models.CharField(
        verbose_name='Название на русском',
        max_length=255,
        help_text='Укажите название на русском',
    )
    description_ru = models.CharField(
        verbose_name='Описание на русском',
        max_length=255,
        blank=True,
        null=True,
        help_text='Укажите описание на русском',
    )
    description_en = models.CharField(
        verbose_name='Описание на английском',
        max_length=255,
        blank=True,
        null=True,
        help_text='Укажите описание на английском',
    )
    description_ch = models.CharField(
        verbose_name='Описание на китайском',
        max_length=255,
        blank=True,
        null=True,
        help_text='Укажите описание на китайском',
    )

    cost = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2,
        help_text='Укажите цену',
    )

    is_publish = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Укажите опубликовано ли блюдо',
    )

    additional = models.ManyToManyField(
        'self',
        verbose_name='Дополнительные товары',
        symmetrical=False,
        related_name='additional_from',
        blank=True,
        help_text='Укажите дополнительные товары',
    )

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
