import unicodedata
import uuid

from django.db import models


class LocationManager(models.Manager):
    def get_queryset(self):
        return LocationQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class LocationQuerySet(models.QuerySet):

    def normalize_text(self, text):
        return (
            unicodedata.normalize("NFKD", text)
            .encode("ASCII", "ignore")
            .decode()
            .casefold()
        )

    def search(self, query):
        normalized_query = self.normalize_text(query)

        return [
            obj
            for obj in self
            if normalized_query in self.normalize_text(obj.search_text)
        ]


class Country(models.Model):

    class DeleteStatus(models.TextChoices):
        ACTIVE = False, "Active"
        DELETED = True, "Deleted"

    id: int
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(max_length=100)
    search_text = models.CharField(max_length=100)
    search_count = models.IntegerField()
    code = models.CharField(max_length=2)
    phone_code = models.CharField(max_length=5)

    is_deleted = models.BooleanField(
        choices=DeleteStatus.choices, default=False, verbose_name="Is Deleted"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    objects = LocationManager()

    def __str__(self):
        return f"Country-{self.pk}: " + self.name

    class Meta:
        verbose_name_plural = "Countries"
        verbose_name = "Country"
        db_table = "country"
        ordering = ["-id"]


class City(models.Model):

    class DeleteStatus(models.TextChoices):
        ACTIVE = False, "Active"
        DELETED = True, "Deleted"

    id: int
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(max_length=100)
    search_text = models.CharField(max_length=100)
    search_count = models.IntegerField()

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="cities", verbose_name="Country"
    )

    is_deleted = models.BooleanField(
        choices=DeleteStatus.choices, default=False, verbose_name="Is Deleted"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    objects = LocationManager()

    def __str__(self):
        return f"City-{self.pk}: " + self.name

    class Meta:
        verbose_name_plural = "Cities"
        verbose_name = "City"
        db_table = "city"
        ordering = ["-id"]


class Airport(models.Model):

    class DeleteStatus(models.TextChoices):
        ACTIVE = False, "Active"
        DELETED = True, "Deleted"

    id: int
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(max_length=100)
    search_text = models.CharField(max_length=100)
    search_count = models.IntegerField()
    code = models.CharField(max_length=2)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="airports",
        verbose_name="Country",
    )
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="airports", verbose_name="City"
    )

    is_deleted = models.BooleanField(
        choices=DeleteStatus.choices, default=False, verbose_name="Is Deleted"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    objects = LocationManager()

    def __str__(self):
        return f"Airport-{self.pk}: " + self.name

    class Meta:
        verbose_name_plural = "Airports"
        verbose_name = "Airport"
        db_table = "airport"
        ordering = ["-id"]
