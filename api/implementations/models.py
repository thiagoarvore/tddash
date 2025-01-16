from accounts.models import User
from django.db import models
from django.utils.timezone import now
from products.models import Product
from services.basemodel import BaseModel
from suppliers.models import Supplier

MANAGEMENT_OPTION = {"Cliente": "Cliente", "Think Digital": "Think Digital"}
STATUS_OPTIONS = {
    "Não iniciado": "Não iniciado",
    "Implementação": "Implementação",
    "Validação cliente": "Validação cliente",
    "Concluída": "Concluída",
    "Bloqueada": "Bloqueada",
}
SOLUTIONS_OPTIONS = {
    "Zoox Wi-fi": "Zoox Wi-fi",
    "Propz": "Propz",
}


class Implementation(BaseModel):
    account_manager = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="implementations",
        blank=True,
        null=True,
        default=None,
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="implementations"
    )
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    mac = models.CharField(max_length=100, null=True, blank=True)
    client = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, default="unknow")
    unit = models.CharField(max_length=50, default="Sede", blank=True, null=True)
    address = models.CharField(max_length=300)
    building_area = models.CharField(max_length=200, blank=True, null=True)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name="implementations",
        default=None,
        blank=True,
        null=True,
    )
    solution = models.CharField(
        max_length=40,
        choices=SOLUTIONS_OPTIONS,
        default="Zoox Wi-Fi",
        blank=True,
        null=True,
    )
    license = models.CharField(max_length=50, default="unknow")
    license_expiration_date = models.DateField(default="2025-12-31")
    status = models.CharField(
        max_length=50, choices=STATUS_OPTIONS, default="Não iniciado"
    )
    management = models.CharField(
        max_length=30, choices=MANAGEMENT_OPTION, default="Think Digital"
    )
    billing_date = models.DateField(default="2025-12-31", blank=True, null=True)
    unifi_url_controller = models.CharField(
        max_length=500, default="unknow", blank=True, null=True
    )
    unifi_access = models.CharField(
        max_length=200, default="unknow", blank=True, null=True
    )
    unifi_password = models.CharField(
        max_length=200, default="unknow", blank=True, null=True
    )
    unifi_site_unity = models.CharField(
        max_length=200, default="unknow", blank=True, null=True
    )
    unifi_management_ip = models.CharField(
        max_length=200, default="unknow", blank=True, null=True
    )
    unifi_observations = models.CharField(
        max_length=500, default="unknow", blank=True, null=True
    )

    @property
    def days_to_expires(self):
        today = now().date()
        return (self.license_expiration_date - today).days

    def __str__(self):
        return f"{self.product} - {self.client}: {self.building_area}"

    class Meta:
        ordering = ["client"]
