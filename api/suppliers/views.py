from rest_framework import viewsets
from .serializers import SupplierSerializer
from .models import Supplier

class SupplierViewSet(viewsets.ModelViewSet):

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()