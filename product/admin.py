from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)   
class ProductAdmin(admin.ModelAdmin):
    """
    This class is used to allow the admin to edit certain aspects of the product information such as the title, the price, and the quantity of a product.
    """
    list_display = ('title', 'price', 'quantity')