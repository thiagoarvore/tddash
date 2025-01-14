from django.db import models

from products.models import Product
from services.basemodel import BaseModel


class Outflow(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="outflows"
    )
    quantity = models.PositiveSmallIntegerField()
    selling_price = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    implemented = models.BooleanField()

    class Meta:
        ordering = ["product"]

    def __str__(self):
        return f"{self.product}"
