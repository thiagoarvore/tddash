from rest_framework import viewsets

from .models import Implementation
from .serializers import ImplementationSerializer


class ImplementationViewSet(viewsets.ModelViewSet):

    serializer_class = ImplementationSerializer
    queryset = Implementation.objects.all()
