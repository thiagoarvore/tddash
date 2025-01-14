from rest_framework import viewsets

from .models import Supplier
from .serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
