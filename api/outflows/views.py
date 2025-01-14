from rest_framework import viewsets
from .serializers import OutflowSerializer
from .models import Outflow

class OutflowViewSet(viewsets.ModelViewSet):

    serializer_class = OutflowSerializer
    queryset = Outflow.objects.all()