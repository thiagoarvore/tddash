from brands.views import BrandViewSet
from categories.views import CategoryViewSet
from django.contrib import admin
from django.urls import include, path
from implementations.views import ImplementationViewSet
from inflows.views import InflowViewSet
from outflows.views import OutflowViewSet
from products.views import ProductViewSet
from rest_framework.routers import DefaultRouter
from suppliers.views import SupplierViewSet

router = DefaultRouter()
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"suppliers", SupplierViewSet, basename="supplier")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"inflows", InflowViewSet, basename="inflow")
router.register(r"outflows", OutflowViewSet, basename="outflow")
router.register(r"implementations", ImplementationViewSet, basename="implementation")

urlpatterns = [path("admin/", admin.site.urls), path("api/v1/", include(router.urls))]
