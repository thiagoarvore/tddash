from rest_framework import serializers

from .models import Product
from brands.serializers import Brand, BrandSerializer
from categories.serializers import Category, CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = (
            "name",
            "brand",
            "category",
            "quantity",
            "serial_number",
            "mac",
            'id'
        )
        read_only_fields = ('id', 'quantity')
    
    def to_representation(self, instance):
        """Personaliza a saída para exibir detalhes no GET"""
        representation = super().to_representation(instance)
        # Adiciona detalhes completos para brand e category
        representation["brand"] = BrandSerializer(instance.brand).data
        representation["category"] = CategorySerializer(instance.category).data
        return representation
