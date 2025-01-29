from django.core.management.base import BaseCommand
from location.models import Airport, City, Country


class Command(BaseCommand):
    help = "Tüm modeller için search_text alanlarını doldurur."

    def set_search_text(self):

        countries = Country.objects.all()
        for country in countries:
            country.search_text = country.name
            country.save()

        cities = City.objects.all()
        for city in cities:
            city.search_text = city.name + " " + city.country.name
            city.save()

        airports = Airport.objects.all()
        for airport in airports:
            airport.search_text = (
                airport.name + " " + airport.city.name + " " + airport.city.country.name
            )
            airport.save()

    def handle(self, *args, **options):
        self.set_search_text()
        self.stdout.write(self.style.SUCCESS("Search textler oluşturuldu."))
