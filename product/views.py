from unicodedata import category
from django.shortcuts import render, get_object_or_404
from product import serializers
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serializers import ProductSerializer, BrandSerializer, BrandModelSerializer, FaqSerializer
from .models import FAQ, BrandModel, Product, Brand

# class ProductPagination(PageNumberPagination):
#     page_size = 1

class ProductsList(APIView, PageNumberPagination):
    # pagination_class = ProductPagination

    def get(self, request, brand_slug=None, brand_model_slug=None, format=None):
        products = Product.objects.all().order_by('-id')[:4]
        if brand_slug:
            products = Product.objects.filter(brandmodel__category__slug=brand_slug)
            
        elif brand_model_slug:
            products = Product.objects.filter(brandmodel__slug=brand_model_slug)
        
        results = self.paginate_queryset(products, request)
        serializer = ProductSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, brandmodel, product_slug):
        # product = Product.objects.get(slug=product_slug)
        product = get_object_or_404(Product, slug=product_slug, brandmodel__slug=brandmodel)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class BrandList(APIView):
    def get(self, request, format=None):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)


class BrandModelList(APIView):
    def get(self, request, brand_slug, format=None):
        brands = BrandModel.objects.filter(category__slug=brand_slug)
        serializer = BrandModelSerializer(brands, many=True)
        return Response(serializer.data)


class BrandModelProductsList(APIView, PageNumberPagination):
    # pagination_class = ProductPagination

    def get(self, request, brand_model_slug):
        products = Product.objects.filter(brandmodel__slug=brand_model_slug)
        results = self.paginate_queryset(products, request)
        serializer = ProductSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)



class FaqList(APIView):
    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FaqSerializer(faqs, many=True)
        return Response(serializer.data)