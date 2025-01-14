from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from brands.views import BrandViewSet
from categories.views import CategoryViewSet
from inflows.views import InflowViewSet
from outflows.views import OutflowViewSet
from products.views import ProductViewSet
from suppliers.views import SupplierViewSet

router = DefaultRouter()
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"suppliers", SupplierViewSet, basename="supplier")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"inflows", InflowViewSet, basename="inflow")
router.register(r"outflows", OutflowViewSet, basename="outflow")

urlpatterns = [path("admin/", admin.site.urls), path("api/v1/", include(router.urls))]
