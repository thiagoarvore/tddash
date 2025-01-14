from django.contrib import admin

from .models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "cost_price", "supplier")
    search_fields = (
        "product",
        "supplier",
    )
