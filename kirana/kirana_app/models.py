from django.db import models


# Create your models here.
SIZE_CHOICES = [('SMALL','SMALL'),('MEDIUM','MEDIUM'),('LARGE','LARGE')]


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    shop_title = models.CharField(max_length=100, blank=True, default='')
    linenos = models.BooleanField(default=False)
    shop_size = models.CharField(choices=SIZE_CHOICES, default='SMALL', max_length=100)
    catalogue = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    product_title = models.CharField(max_length=100, blank=True, default='')
    shop_size = models.CharField(choices=SIZE_CHOICES, default='SMALL', max_length=100)
    linenos = models.BooleanField(default=False)
    catalogue = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']

class Mapping(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey(
        "Products", on_delete=models.CASCADE)
    shop_id = models.ForeignKey(
        "Shop", on_delete=models.CASCADE)
    stock_status = models.CharField(default='OUT', max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ['created']
    
    @property
    def product_name(self):
        return self.product_id.product_title

    @property
    def shop_name(self):
        return self.shop_id.shop_title