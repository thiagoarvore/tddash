from django.contrib.auth.models import AbstractUser

from services.basemodel import BaseModel


class User(BaseModel, AbstractUser):

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name else self.email
