from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to = 'category', default ='category/pic.jpg')

    def __str__(self):
        return self.title

    class Meta:
            db_table = 'Category'
            managed = True
            verbose_name = 'Category'
            verbose_name_plural = 'Categories'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=50)
    p_model = models.CharField(max_length=50)
    p_price = models.IntegerField()
    p_discount = models.FloatField()
    p_img = models.ImageField(upload_to = 'product',default= 'product/pix.jpg')
    des = models.TextField()
    trending = models.BooleanField()
    latest = models.BooleanField()
    p_min = models.IntegerField()
    p_max = models.IntegerField()
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.p_name

    class Meta:
            db_table = 'Product'
            managed = True
            verbose_name = 'Product'
            verbose_name_plural = 'Products'


class Shopcart(models.Model):
    product = models.ForeignKey(Product,on_delete =models.CASCADE)
    s_name = models.CharField(max_length =50)
    s_price = models.IntegerField()
    s_quantity = models.IntegerField()
    s_amount = models.IntegerField()
    




