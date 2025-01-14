from rest_framework import viewsets

from .models import Outflow
from .serializers import OutflowSerializer


class OutflowViewSet(viewsets.ModelViewSet):

    serializer_class = OutflowSerializer
    queryset = Outflow.objects.all()
