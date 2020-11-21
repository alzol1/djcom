from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

	
    def __str__(self):
        return self.title

		
		
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField('Наименование', max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

	
    def __str__(self):
        return self.title


