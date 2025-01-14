from rest_framework import viewsets
from .serializers import BrandSerializer
from .models import Brand

class BrandViewSet(viewsets.ModelViewSet):

    serializer_class = BrandSerializer
    queryset = Brand.objects.all()