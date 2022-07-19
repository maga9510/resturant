from django.contrib import admin
from order.models import order, cart

admin.site.register(order)
admin.site.register(cart)
