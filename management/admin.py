from django.contrib import admin

from inventory.models import Product
from management.models import Sale

# Register your models here.
admin.site.register(Product)
admin.site.register(Sale)