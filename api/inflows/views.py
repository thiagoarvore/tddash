from rest_framework import viewsets
from .serializers import InflowSerializer
from .models import Inflow

class InflowViewSet(viewsets.ModelViewSet):

    serializer_class = InflowSerializer
    queryset = Inflow.objects.all()