from rest_framework import viewsets

from .models import User
from .serializers import AccountSerializer


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    queryset = User.objects.all()
