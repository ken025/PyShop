from django.contrib import admin
from .models import Product

# Register your models here.
# Customize
class ProductAdmin(admin.ModelAdmin):
    # specify what columns will be visible (model's attributes)
    list_display = ('name', 'price', 'stock')
# tell django we want to manage our products in the admin area
admin.site.register(Product, ProductAdmin)
# generates form