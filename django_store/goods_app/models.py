from django.db import models

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('goods_app:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class GoodItems(models.Model):
    UNITS = (
        (1, 'шт.'),
        (2, 'кг.'),
    )

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название товара', max_length=255)
    created_at = models.DateTimeField(verbose_name='Дата поступления', auto_created=True, auto_now_add=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=4, decimal_places=2)
    unit = models.PositiveIntegerField(verbose_name='Еденица измерения', choices=UNITS)
    slug = models.SlugField(max_length=255)
    supplier = models.CharField(verbose_name='Имя поставщика', max_length=255)

    class Meta:
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
