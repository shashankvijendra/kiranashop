from django.shortcuts import render
from rest_framework.views import APIView
from kirana_app.models import Shop, Products, Mapping
from kirana_app.serializer import ShopSerializer, ProductsSerializer, MappingSerializer, MappingSerializers
from rest_framework import status
from rest_framework.response import Response
from django.http import  Http404, JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
# @api_view(['GET', 'PUT', 'DELETE'])

class ShopList(APIView):
    """
    Shop list and shop name update
    """
    def get(self, request, format=None):
        snippets = Shop.objects.all()
        serializer = ShopSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShopDetail(APIView):
    """
    Retrieve, update or delete a shop details based on specified shop 
    """
    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ShopSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ShopSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(APIView):
    """
    Product list and Product name adding to database
    """
    def get(self, request):
        snippets = Products.objects.all()
        serializer = ProductsSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    Retrieve, update or delete a Product instance.
    """
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProductsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProductsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Product_availableDetail(APIView):
    """
        Display List of eligible product
    """

    def get(self, request, shop_size):
        snippets = Products.objects.filter(shop_size=shop_size)
        serializer = ProductsSerializer(snippets, many=True)
        return Response(serializer.data)


class Product_Mapping_Shop(APIView):
    """
    Product and shop map with price and stock status
    """
    def get(self, request):
        snippets = Mapping.objects.all()
        serializer = MappingSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        pk = request.data['product_id']
        sk = request.data['shop_id']
        Shop_res = Shop.objects.filter(id=pk).values('shop_size')
        product_res = Products.objects.filter(id=sk,shop_size__in=Shop_res).exists()
        if not product_res:
            raise Http404
        if Mapping.objects.filter(product_id=pk,shop_id=sk).exists():
            return JsonResponse({'status':'already exist'})
        serializer = MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductMapping_each(APIView):
    """
    Retrieve, update or delete a Product instance.
    """
    def get_object(self, pk, sk):
        try:
            Shop_res = Shop.objects.filter(id=pk).values('shop_size')
            product_res = Products.objects.filter(id=sk,shop_size__in=Shop_res).exists()
            print(product_res)
            return Mapping.objects.get(product_id=pk,shop_id=sk)
        except Mapping.DoesNotExist:
            raise Http404

    def get(self, request, pk, sk):
        snippet = self.get_object(pk, sk)
        serializer = MappingSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, sk):
        snippet = self.get_object(pk, sk)
        serializer = MappingSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, sk):
        snippet = self.get_object(pk, sk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Retrieve_product(APIView):
    """
    Retrieve all updated Product details
    """

    def get(self, request, pk):
        snippets = Mapping.objects.filter(shop_id=pk)
        serializer = MappingSerializers(snippets, many=True)
        return Response(serializer.data)


class Retrieve_serviceable_product(APIView):
    """
    Retrieve, serviceable with updated Product details
    """

    def get(self, request, pk):
        snippets = Mapping.objects.filter(shop_id=pk, stock_status='IN')
        serializer = MappingSerializers(snippets, many=True)
        return Response(serializer.data)