from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField('Имя', max_length=50)
    price = models.FloatField('Цена', default=0)
    image = models.URLField('Картинка', max_length=200)
    release_date = models.DateField('Дата релиза', auto_now_add=True)
    lte_exists = models.BooleanField('Поддержка LTE', default=False)
    slug = models.SlugField('Slug', unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            name_to_slugify = self.name if self.name else "без названия"
            self.slug = slugify(name_to_slugify)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
