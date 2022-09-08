from django.contrib import admin
from product.models import *

admin.site.register(category)
admin.site.register(unit)
admin.site.register(product)
admin.site.register(product_amount)
admin.site.register(category_join_product)


