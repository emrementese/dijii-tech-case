from django.contrib import admin

from .models import Airport, City, Country

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Airport)
