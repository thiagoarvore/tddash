from brands.models import Brand
from categories.models import Category
from django.db import models
from services.basemodel import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products")
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    mac = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    @property
    def quantity(self):
        inflow_exists = self.inflows.exists()
        outflow_exists = self.outflows.exists()

        if not inflow_exists and not outflow_exists:
            return 0

        total_inflows = (
            self.inflows.aggregate(total=models.Sum("quantity"))["total"] or 0
        )
        total_outflows = (
            self.outflows.aggregate(total=models.Sum("quantity"))["total"] or 0
        )

        return total_inflows - total_outflows

    def __str__(self):
        return f"{self.name}"
