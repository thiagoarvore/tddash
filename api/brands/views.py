from rest_framework import viewsets

from .models import Brand
from .serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):

    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
