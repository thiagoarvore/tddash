from rest_framework import viewsets

from .models import Inflow
from .serializers import InflowSerializer


class InflowViewSet(viewsets.ModelViewSet):

    serializer_class = InflowSerializer
    queryset = Inflow.objects.all()
