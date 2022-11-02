from django.contrib import admin
from . models import Category, Product,Shopcart

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','img']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','p_name','p_model','p_price','p_discount','p_img','des','trending','latest','p_min','p_max','available']

@admin.register(Shopcart)
class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['product','s_name','s_price','s_quantity','s_amount']

