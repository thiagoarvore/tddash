from accounts.views import UserViewSet
from brands.views import BrandViewSet
from categories.views import CategoryViewSet
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from implementations.views import ImplementationViewSet
from inflows.views import InflowViewSet
from outflows.views import OutflowViewSet
from products.views import ProductViewSet
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from suppliers.views import SupplierViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"suppliers", SupplierViewSet, basename="supplier")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"inflows", InflowViewSet, basename="inflow")
router.register(r"outflows", OutflowViewSet, basename="outflow")
router.register(r"implementations", ImplementationViewSet, basename="implementation")
router.register(r"accounts", UserViewSet, basename="account")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path(
        "api/v1/authentication/token/",
        TokenObtainPairView.as_view(),
        name="token-obtain-pair",
    ),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
