from autoslug import AutoSlugField
from django.db import models


class Trip(
    models.Model,
):
    # Surrogate Keys

    id = models.AutoField(
        primary_key=True,
    )

    slug = AutoSlugField(
        populate_from="get_slug",
        unique_with=(
            "start__year",
            "start__month",
            "start__day",
        ),
    )

    # Natural Keys

    name = models.CharField(
        blank=False,
        max_length=64,
        null=False,
    )

    start = models.DateField(
        blank=False,
        null=False,
    )

    # Fields

    end = models.DateField(
        blank=True,
        max_length=25,
        null=True,
    )

    open_location_code = models.CharField(  # noqa: DJ001
        blank=True,
        max_length=25,
        null=True,
    )

    # Classes

    class Meta:
        unique_together = ("start", "slug")

    # Methods

    def __str__(
        self,
    ) -> str:
        return self.name

    @property
    def description(
        self,
    ) -> str:
        return f"A {self.end - self.start} trip"

    def get_slug(
        self,
    ) -> str:
        return self.name

    def get_key(
        self,
    ) -> dict[str, str]:
        return {
            "trip_slug": str(self.slug),
            "trip_year": str(self.start.year).zfill(4),
            "trip_month": str(self.start.month).zfill(2),
            "trip_day": str(self.start.day).zfill(2),
        }
