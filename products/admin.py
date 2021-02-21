from django.contrib import admin
from .models import Product, Offer

# Register your models here.
# Customize
class ProductAdmin(admin.ModelAdmin):
    # specify what columns will be visible (model's attributes)
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
# tell django we want to manage our products in the admin area
admin.site.register(Product, ProductAdmin)
admin.site.register( Offer, OfferAdmin)
# generates form