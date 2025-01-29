from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularJSONAPIView as JsonView
from drf_spectacular.views import SpectacularSwaggerView as SwaggerView
from location.views import LocationViewset
from rest_framework import routers

from .views import LoginView

api_router = routers.DefaultRouter()
api_router.register(r"location", LocationViewset, basename="location")

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("", include(api_router.urls)),
    path(
        "api/swagger-json",
        JsonView.as_view(),
        name="swagger-json",
    ),
    re_path(
        r"api/$",
        SwaggerView.as_view(url_name="swagger-json"),
        name="swagger-ui",
    ),
]
