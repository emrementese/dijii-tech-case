from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import City, Country


def get_dynamic_serializer(data_model):
    """Her model için dinamik bir serializer oluşturur."""

    class DynamicSerializer(serializers.ModelSerializer):
        class Meta:
            model = data_model
            fields = "__all__"

    return DynamicSerializer


class MultiCountryCodeSerializer(serializers.Serializer):
    country_codes = serializers.ListField(child=serializers.CharField(), required=True)

    def validate(self, attrs):
        codes = attrs.get("country_codes")
        country_list = []
        try:
            for code in codes:
                country = Country.objects.get(code=code)
                country_list.append(country)
        except Country.DoesNotExist:
            raise serializers.ValidationError("Invalid country code")

        attrs["country_codes"] = country_list
        return attrs


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name", "search_count"]


class MostSearchedCitySerializer(serializers.ModelSerializer):

    @extend_schema_field(CitySerializer(many=True))
    def get_cities(self, obj: Country):
        cities = obj.cities.all().order_by("-search_count")[:5]
        return CitySerializer(cities, many=True).data

    cities = serializers.SerializerMethodField("get_cities")

    class Meta:
        model = Country
        fields = ["name", "search_count", "cities"]


class CountryRatioSerializer(serializers.ModelSerializer):

    @extend_schema_field(serializers.FloatField)
    def get_search_ratio(self, obj: Country):
        cities = obj.cities.all()
        airports = obj.airports.all()
        total_cities_search = sum([city.search_count for city in cities])
        total_airports_search = sum([airport.search_count for airport in airports])
        if total_airports_search == 0:
            return 0
        return total_cities_search / total_airports_search

    search_ratio = serializers.SerializerMethodField("get_search_ratio")

    class Meta:
        model = Country
        fields = [
            "uuid",
            "name",
            "search_count",
            "code",
            "created_at",
            "updated_at",
            "is_deleted",
            "search_ratio",
        ]
