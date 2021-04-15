from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'  # to change data name in admin

    name = models.CharField(max_length=254)
    shop_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_shop_name(self):
        return self.shop_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
