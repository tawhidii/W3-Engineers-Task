from django.contrib import admin
from .models import Product
# Registering Product model to admin here
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','image','price']

admin.site.register(Product,ProductAdmin)