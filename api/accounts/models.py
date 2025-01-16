from django.contrib.auth.models import AbstractUser
from django.db import models
from services.basemodel import BaseModel

SECTOR_CHOICES = {
    "Comercial": "Comercial",
    "Financeiro": "Financeiro",
    "Jurídico": "Jurídico",
    "Técnico": "Técnico",
    "Suporte": "Suporte",
}


class User(BaseModel, AbstractUser):
    sector = models.CharField(
        max_length=50, choices=SECTOR_CHOICES, blank=True, null=True, default="Suporte"
    )

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name else self.email
