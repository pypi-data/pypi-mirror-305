from datetime import datetime, timedelta

from autoslug import AutoSlugField
from django.db import models
from timezone_field import TimeZoneField

from illallangi.data.aviation.models import Airline, Airport


class Flight(
    models.Model,
):
    # Surrogate Keys

    id = models.AutoField(
        primary_key=True,
    )

    slug = AutoSlugField(
        populate_from="get_slug",
        unique_with=(
            "departure__year",
            "departure__month",
            "departure__day",
        ),
    )

    # Natural Keys

    departure = models.DateTimeField(
        blank=False,
        null=False,
    )

    flight_number = models.CharField(
        blank=False,
        max_length=6,
        null=False,
    )

    # Fields

    airline = models.ForeignKey(
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="flights",
        to=Airline,
    )

    arrival_timezone = TimeZoneField(
        blank=False,
        null=False,
    )

    arrival = models.DateTimeField(
        blank=False,
        max_length=25,
        null=False,
    )

    departure_timezone = TimeZoneField(
        blank=False,
        null=False,
    )

    destination = models.ForeignKey(
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="destination_flights",
        to=Airport,
    )

    destination_city = models.CharField(
        blank=False,
        max_length=255,
        null=False,
    )

    destination_gate = models.CharField(  # noqa: DJ001
        blank=True,
        max_length=255,
        null=True,
    )

    destination_terminal = models.CharField(  # noqa: DJ001
        blank=True,
        max_length=255,
        null=True,
    )

    flight_class = models.CharField(  # noqa: DJ001
        blank=True,
        max_length=255,
        null=True,
    )

    origin = models.ForeignKey(
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="originating_flights",
        to=Airport,
    )

    origin_city = models.CharField(
        blank=False,
        max_length=255,
        null=False,
    )

    origin_gate = models.CharField(  # noqa: DJ001
        blank=True,
        max_length=255,
        null=True,
    )

    origin_terminal = models.CharField(  # noqa: DJ001
        blank=True,
        max_length=255,
        null=True,
    )

    passenger = models.CharField(  # noqa: DJ001
        blank=True,
        max_length=255,
        null=True,
    )

    seat = models.CharField(  # noqa: DJ001
        blank=True,
        max_length=3,
        null=True,
    )

    sequence_number = models.CharField(
        blank=False,
        max_length=3,
        null=False,
    )

    trip = models.ForeignKey(
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="flights",
        to="Trip",
    )

    # Classes

    class Meta:
        unique_together = ("departure", "flight_number")

    # Methods

    def __str__(
        self,
    ) -> str:
        return self.flight_number

    @property
    def description(
        self,
    ) -> str:
        return f"A {self.airline.label or self.airline} flight from {self.origin_city} to {self.destination_city}"

    @property
    def boarding(
        self,
    ) -> datetime:
        return self.departure - timedelta(minutes=30)

    @property
    def boarding_timezone(
        self,
    ) -> str:
        return self.departure_timezone

    @property
    def boarding_date_local(
        self,
    ) -> str:
        return self.boarding.astimezone(self.boarding_timezone).strftime("%d%b")

    @property
    def boarding_time_local(
        self,
    ) -> str:
        return self.boarding.astimezone(self.boarding_timezone).strftime("%H%M")

    @property
    def departure_date_local(
        self,
    ) -> str:
        return self.departure.astimezone(self.departure_timezone).strftime("%d%b")

    @property
    def departure_time_local(
        self,
    ) -> str:
        return self.departure.astimezone(self.departure_timezone).strftime("%H%M")

    @property
    def arrival_date_local(
        self,
    ) -> str:
        return self.arrival.astimezone(self.arrival_timezone).strftime("%d%b")

    @property
    def arrival_time_local(
        self,
    ) -> str:
        return self.arrival.astimezone(self.arrival_timezone).strftime("%H%M")

    def get_slug(
        self,
    ) -> str:
        return self.flight_number.replace(" ", "")
