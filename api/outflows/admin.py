from django.contrib import admin

from .models import Outflow


@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "selling_price", "implemented")
    search_fields = ("product", "supplier", "implemented")
