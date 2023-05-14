from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # def get_url(self):
    #     return "http://127.0.0.1:8000/store/" + str(self.slug)

    def get_url(self):
        return reverse('category_product', args=[self.slug])

    def __str__(self):
        return self.category_name
