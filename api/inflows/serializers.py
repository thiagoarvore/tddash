from products.serializers import Product, ProductSerializer
from rest_framework import serializers
from suppliers.serializers import Supplier, SupplierSerializer

from .models import Inflow


class InflowSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())

    class Meta:
        model = Inflow
        fields = (
            "id",
            "product",
            "supplier",
            "quantity",
            "cost_price",
        )
        read_only_fields = ("id",)

    def to_representation(self, instance):
        """Personaliza a saída para exibir detalhes no GET"""
        representation = super().to_representation(instance)
        # Adiciona detalhes completos para brand e category
        representation["product"] = ProductSerializer(instance.product).data
        representation["supplier"] = SupplierSerializer(instance.supplier).data
        return representation
