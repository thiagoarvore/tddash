from django.db import models
from services.basemodel import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"
