from django.contrib import admin
from order.models import order, cart


@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "phone", "organization_table", "status", "people_number", "created", "paymants")


@admin.register(cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("orders", "product_amount", "amount")



