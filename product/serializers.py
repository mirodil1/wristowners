from pyexpat import model
from rest_framework import serializers

from .models import FAQ, Brand, BrandModel,  Product


class BrandModelSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)
    class Meta:
        model = BrandModel
        fields = (
            'id',
            'name',
            'slug',
        )


class ProductSerializer(serializers.ModelSerializer):
    brandmodel = BrandModelSerializer()
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'series',
            'brandmodel',
            'gender',
            'crystal',
            'strap', 
            'size',
            'case',
            'movement',
            'clasp',
            'bazel',
            'slug',
            'description',
            'price',
            'image',
            'get_image',
            'get_image1',
            'get_image2',
            'get_image3',
            'get_image4',
            'thumbnail',
            'get_absolute_url'
        )


class BrandSerializer(serializers.ModelSerializer):
    brandmodel = BrandModelSerializer(many=True)
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'brandmodel',
            'slug',
            # 'category',
        )


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = (
            'id',
            'question',
            'answer',
        )

