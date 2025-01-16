from django.contrib import admin

from .models import Implementation


@admin.register(Implementation)
class ImplementationtAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "serial_number",
        "mac",
        "client",
        "address",
        "building_area",
    )
    search_fields = (
        "product",
        "client",
    )
