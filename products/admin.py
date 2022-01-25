from django.contrib import admin
from .models import Products
from .models import Offer
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
admin.site.register(Products, ProductsAdmin)
admin.site.register(Offer, OfferAmin)

