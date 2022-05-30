from django.db import models


class GoodItems(models.Model):
    UNITS = (
        (1, 'шт.'),
        (2, 'кг.'),
    )

    title = models.CharField(verbose_name='Название товара', max_length=255)
    created_at = models.DateTimeField(verbose_name='Дата поступления', auto_created=True, auto_now_add=True)
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    unit = models.PositiveIntegerField(verbose_name='Еденица измерения', choices=UNITS)
    supplier = models.CharField(verbose_name='Имя поставщика', max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
