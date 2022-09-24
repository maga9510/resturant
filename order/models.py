from django.db import models
from product.models import *
from organization.models import *
from datetime import datetime
from django.utils import timezone

class order(models.Model):
    organization_table = models.ForeignKey(organization_table, help_text='Which table the client chose', verbose_name='table number',  on_delete=models.PROTECT)
    people_number = models.PositiveSmallIntegerField(verbose_name='Peopls', help_text='How many clients')
    STATUS = (
        (1, 'new'),
        (2, 'pending'),
        (3, 'preparing'),
        (4, 'cancellation'),
        
    )
    name = models.CharField(max_length= 64, verbose_name="Client name", null=False)
    last_name = models.CharField(max_length=64, verbose_name="Client lastname", null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name="Phone number")
    status = models.PositiveSmallIntegerField(verbose_name='Order status', choices=STATUS, default=1)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    PAYMANTS = (
        ("Cash", 'Cash'),
        ("Terminal", 'Terminal'),
        ("PayMe", 'PayMe'),
        ("Click", 'Click'),
    )
    paymants = models.CharField(verbose_name="Paymants", choices=PAYMANTS, max_length=10)



class cart(models.Model):
    orders = models.ForeignKey(order, on_delete=models.CASCADE)
    product_amount = models.ForeignKey(product_amount, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(null=False)
    craete_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Product name added to cart {self.product_amount.product}'

