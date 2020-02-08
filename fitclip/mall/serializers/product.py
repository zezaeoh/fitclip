from rest_framework import serializers

from fitclip.mall.models.product import Product, ProductDetail


class ProductSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj: Product):
        return obj.detail.thumbnail.url

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
