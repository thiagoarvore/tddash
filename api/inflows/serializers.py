from rest_framework import serializers

from .models import Inflow


class InflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inflow
        fields = (
            "product",
            "supplier",
            "quantity",
            "cost_price",
        )
