from django.db import models
from product.models import *
from organization.models import *

class order(models.Model):
    organization_table = models.ForeignKey(organization_table, help_text='Which table the client chose', verbose_name='table number',  on_delete=models.PROTECT)
    people_number = models.PositiveSmallIntegerField(verbose_name='Peopls', help_text='How many clients')
    STATUS = (
        (1, 'new'),
        (2, 'pending'),
        (3, 'preparing'),
        (4, 'cancellation'),
        
    )
    status = models.PositiveSmallIntegerField(verbose_name='Order status', choices=STATUS)
    PAYMANTS = (
        (1, 'Cash'),
        (2, 'Terminal'),
        (3, 'PayMe'),
        (4, 'Click'),
    )
    paymants = models.PositiveSmallIntegerField(verbose_name="Paymants", choices=PAYMANTS)

class cart(models.Model):
    orders = models.ForeignKey(order, on_delete=models.CASCADE)
    product_amount = models.ForeignKey(product_amount, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(null=False)

    def __str__(self) -> str:
        return f'Product name added to cart {self.product_amount.product}'

