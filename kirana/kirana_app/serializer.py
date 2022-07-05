from rest_framework import serializers
from kirana_app.models import Shop, Products, Mapping


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'shop_title', 'linenos', 'shop_size', 'catalogue']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'product_title', 'shop_size', 'linenos', 'catalogue']


class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = ['product_id', 'shop_id', 'stock_status', 'price']


class MappingSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Mapping
        fields = ['shop_name', 'product_name', 'stock_status', 'price']
