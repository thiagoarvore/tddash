from products.serializers import Product, ProductSerializer
from rest_framework import serializers

from .models import Outflow


class OutflowSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Outflow
        fields = (
            "id",
            "product",
            "implemented",
            "quantity",
            "selling_price",
        )
        read_only_fields = ("id",)

    def to_representation(self, instance):
        """Personaliza a saída para exibir detalhes no GET"""
        representation = super().to_representation(instance)
        # Adiciona detalhes completos para brand e category
        representation["product"] = ProductSerializer(instance.product).data
        return representation
