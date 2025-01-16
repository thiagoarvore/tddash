from products.serializers import Product, ProductSerializer
from suppliers.serializers import Supplier, SupplierSerializer
from rest_framework import serializers

from .models import Implementation


class ImplementationSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    class Meta:
        model = Implementation
        fields = (
            "product",
            "client",
            "cnpj",
            "unit",
            "address",
            "building_area",
            "serial_number",
            "mac",
            "id",
            "solution",
            "license",
            "license_expiration_date",
            "status",
            "management",
            "billing_date",
            "unifi_url_controller",
            "unifi_access",
            "unifi_password",
            "unifi_site_unity",
            "unifi_management_ip",
            "unifi_observations",
            "days_to_expires",
            'supplier'
        )
        read_only_fields = ("id", "days_to_expires", 'supplier')

    def to_representation(self, instance):
        """Personaliza a saída para exibir detalhes no GET"""
        representation = super().to_representation(instance)
        # Adiciona detalhes completos para brand e category
        representation["product"] = ProductSerializer(instance.product).data
        representation["supplier"] = SupplierSerializer(instance.supplier).data
        return representation
