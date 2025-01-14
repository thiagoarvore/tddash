from django.db import models
from products.models import Product
from services.basemodel import BaseModel
from suppliers.models import Supplier


class Inflow(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="inflows"
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, related_name="inflows"
    )
    quantity = models.PositiveSmallIntegerField()
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        ordering = ["product"]

    def __str__(self):
        return f"{self.product}"
