from api.serializers import (
    DefaultExceptionSerializer,
    NotFoundSerializer,
    PermissionDeniedSerializer,
    UnAuthorizedSerializer,
)
from django.apps import apps
from drf_spectacular.utils import (
    OpenApiParameter,
    PolymorphicProxySerializer,
    extend_schema,
    extend_schema_view,
)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.viewsets import GenericViewSet

from .serializers import (
    CountryRatioSerializer,
    MostSearchedCitySerializer,
    MultiCountryCodeSerializer,
    get_dynamic_serializer,
)


@extend_schema_view(
    most_searched_cities=extend_schema(
        request=MultiCountryCodeSerializer,
        responses={
            200: MostSearchedCitySerializer(many=True),
            400: DefaultExceptionSerializer,
            401: UnAuthorizedSerializer,
            403: PermissionDeniedSerializer,
            404: NotFoundSerializer,
        },
    ),
    country_search_ratio=extend_schema(
        request=MultiCountryCodeSerializer,
        responses={
            200: CountryRatioSerializer(many=True),
            400: DefaultExceptionSerializer,
            401: UnAuthorizedSerializer,
            403: PermissionDeniedSerializer,
            404: NotFoundSerializer,
        },
    ),
    location_search=extend_schema(
        request=None,
        parameters=[
            OpenApiParameter(
                name="location_model",
                location=OpenApiParameter.QUERY,
                description="Name of the lcoation model",
                required=True,
                type=str,
                enum=["Country", "City", "Airport"],
            ),
            OpenApiParameter(
                name="search_query",
                location=OpenApiParameter.QUERY,
                description="Search query",
                required=True,
                type=str,
            ),
        ],
        responses={
            200: PolymorphicProxySerializer(
                component_name="LocationSearchResponse",
                serializers={
                    "Country": get_dynamic_serializer(
                        apps.get_model("location", "Country")
                    ),
                    "City": get_dynamic_serializer(apps.get_model("location", "City")),
                    "Airport": get_dynamic_serializer(
                        apps.get_model("location", "Airport")
                    ),
                },
                resource_type_field_name="location_model",
            ),
            400: DefaultExceptionSerializer,
            401: UnAuthorizedSerializer,
            403: PermissionDeniedSerializer,
            404: NotFoundSerializer,
        },
    ),
    select_location=extend_schema(
        request=None,
        parameters=[
            OpenApiParameter(
                name="location_model",
                location=OpenApiParameter.QUERY,
                description="Name of the lcoation model",
                required=True,
                type=str,
                enum=["Country", "City", "Airport"],
            ),
            OpenApiParameter(
                name="location_uuid",
                location=OpenApiParameter.QUERY,
                description="Location UUID",
                required=True,
                type=str,
            ),
        ],
        responses={
            204: None,
            400: DefaultExceptionSerializer,
            401: UnAuthorizedSerializer,
            403: PermissionDeniedSerializer,
            404: NotFoundSerializer,
        },
    ),
    deselect_location=extend_schema(
        request=None,
        responses={
            204: None,
            400: DefaultExceptionSerializer,
            401: UnAuthorizedSerializer,
            403: PermissionDeniedSerializer,
            404: NotFoundSerializer,
        },
    ),
)
class LocationViewset(GenericViewSet):
    http_method_names = ["get", "post", "delete"]
    permission_classes = []  # sizi uğraştırmasın diye boş bıraktım.

    def get_serializer_class(self):
        match self.action:
            case "most_searched_cities" | "country_search_ratio":

                return MultiCountryCodeSerializer

    @action(
        detail=False,
        methods=["get"],
        url_path="location-search",
        url_name="location-search",
    )
    def location_search(self, request: Request, *args, **kwargs) -> Response:
        location_model = request.query_params.get("location_model")
        search_query = request.query_params.get("search_query")

        if location_model is None or search_query is None:
            raise ValidationError("location_model and search_query params are required")

        model = apps.get_model("location", location_model)
        if model is None:
            raise ValidationError("Invalid location_model")

        results = model.objects.search(search_query)

        serializer = get_dynamic_serializer(model)
        results = serializer(results, many=True).data
        return Response(results, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["post"],
        url_path="most-searched-cities",
        url_name="most-searched-cities",
        pagination_class=None,
    )
    def most_searched_cities(self, request: Request, *args, **kwargs) -> Response:
        """
        * Ülke kodlarını validate ettikten sonra en çok aranan 5 şehri ülkeleri ile döner.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_serializer = MostSearchedCitySerializer(
            serializer.validated_data["country_codes"], many=True
        )
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["post"],
        url_path="country-search-ratio",
        url_name="country-search-ratio",
        pagination_class=None,
    )
    def country_search_ratio(self, request: Request, *args, **kwargs) -> Response:
        """
        * Ülke arama oranlarını döner.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_serializer = CountryRatioSerializer(
            serializer.validated_data["country_codes"], many=True
        )
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["get"],
        url_path="select-location",
        url_name="select-location",
    )
    def select_location(self, request: Request, *args, **kwargs) -> Response:
        location_model = request.query_params.get("location_model")
        location_uuid = request.query_params.get("location_uuid")

        if location_model is None or location_uuid is None:
            raise ValidationError(
                "location_model and location_uuid params are required"
            )

        model = apps.get_model("location", location_model)
        if model is None:
            raise ValidationError("Invalid location_model")

        try:
            location = model.objects.get(uuid=location_uuid)
        except model.DoesNotExist:
            raise ValidationError("Invalid location_id")

        match location_model:

            case "Country":
                location.search_count += 1
                location.save()

            case "City":
                location.country.search_count += 1
                location.country.save()

                location.search_count += 1
                location.save()

            case "Airport":
                location.city.country.search_count += 1
                location.city.search_count += 1
                location.city.save()
                location.country.save()
                location.search_count += 1
                location.save()

        response = Response(status=status.HTTP_204_NO_CONTENT)

        response.set_cookie("location_model", location_model, max_age=60 * 60 * 24 * 30)
        response.set_cookie("location_uuid", location.uuid, max_age=60 * 60 * 24 * 30)
        return response

    @action(
        detail=False,
        methods=["delete"],
        url_path="deselect-location",
        url_name="deselect-location",
    )
    def deselect_location(self, request: Request, *args, **kwargs) -> Response:
        response = Response(status=status.HTTP_204_NO_CONTENT)

        response.delete_cookie("location_model")
        response.delete_cookie("location_uuid")
        return response

    def finalize_response(
        self, request: Request, response: Response, *args, **kwargs
    ) -> Response:
        if response.status_code < 400:
            model = request.COOKIES.get("location_model")
            uuid = request.COOKIES.get("location_uuid")

            try:
                location = apps.get_model("location", model).objects.get(uuid=uuid)
            except model.DoesNotExist:
                pass

        match model:

            case "Country":
                location.search_count += 1
                location.save()

            case "City":
                location.country.search_count += 1
                location.country.save()

                location.search_count += 1
                location.save()

            case "Airport":
                location.city.country.search_count += 1
                location.city.search_count += 1
                location.city.save()
                location.country.save()
                location.search_count += 1
                location.save()

        return super().finalize_response(request, response, *args, **kwargs)
