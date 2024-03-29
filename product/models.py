from django.db import models
from organization.models import *
from datetime import datetime

class category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Catigory name', null=False)
    oraganizatsion_id = models.ForeignKey(organizatsion, verbose_name='Which organization product catigoris', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='catigoris_photo/')

    def __str__(self) -> str:
        return self.name


class unit(models.Model):
    name = models.CharField(verbose_name='Unit', max_length=10)
    def __str__(self) -> str:
        return self.name

class product(models.Model):
    name = models.CharField(max_length=64, verbose_name='Product name', null=False)
    unit = models.ForeignKey(unit, on_delete=models.CASCADE)
    description = models.CharField(max_length=264, verbose_name='Description product', null=True)
    photo = models.ImageField(upload_to='product_photo/', blank=True)

    def __str__(self) -> str:
        return self.name

    
class product_amount(models.Model):
    product = models.ForeignKey(product, verbose_name='Which product', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Item title", max_length=20)
    price = models.IntegerField(verbose_name='Price')

    def __str__(self) -> str:
        return f'{self.title}'
    

class category_join_product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Catigoris name {self.category.name} Product name {self.product.name}'


