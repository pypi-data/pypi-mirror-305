from datetime import date, datetime

import diffsync

from illallangi.data.air_transport.models import Flight as DjangoFlight
from illallangi.data.air_transport.models import Trip
from illallangi.data.aviation.models import Airline, Airport


class Flight(
    diffsync.DiffSyncModel,
):
    _modelname = "Flight"
    _identifiers = (
        "departure",
        "flight_number",
    )
    _attributes = (
        "airline__iata",
        "arrival_timezone",
        "arrival",
        "departure_timezone",
        "destination__iata",
        "destination_city",
        "destination_gate",
        "destination_terminal",
        "flight_class",
        "origin__iata",
        "origin_city",
        "origin_gate",
        "origin_terminal",
        "passenger",
        "seat",
        "sequence_number",
        "trip__name",
        "trip__start",
    )

    pk: int

    departure: datetime
    flight_number: str

    airline__iata: str
    arrival_timezone: str
    arrival: datetime
    departure_timezone: str
    destination__iata: str
    destination_city: str
    destination_gate: str | None
    destination_terminal: str | None
    flight_class: str | None
    origin__iata: str
    origin_city: str
    origin_gate: str | None
    origin_terminal: str | None
    passenger: str | None
    seat: str | None
    sequence_number: str
    trip__name: str
    trip__start: date

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Flight":
        airline = Airline.objects.get_or_create(
            iata=attrs["airline__iata"],
        )[0]

        destination = Airport.objects.get_or_create(iata=attrs["destination__iata"])[0]

        origin = Airport.objects.get_or_create(
            iata=attrs["origin__iata"],
        )[0]

        trip = Trip.objects.get_or_create(
            name=attrs["trip__name"],
            start=attrs["trip__start"],
        )[0]

        obj = DjangoFlight.objects.update_or_create(
            **ids,
            defaults={
                **{
                    k: v
                    for k, v in attrs.items()
                    if k
                    not in [
                        "airline__iata",
                        "destination__iata",
                        "origin__iata",
                        "trip__name",
                        "trip__start",
                    ]
                },
                "airline": airline,
                "destination": destination,
                "origin": origin,
                "trip": trip,
            },
        )[0]

        return super().create(
            adapter,
            {
                "pk": obj.pk,
                **ids,
            },
            attrs,
        )

    def update(
        self,
        attrs: dict,
    ) -> "Flight":
        airline = Airline.objects.get_or_create(
            iata=attrs["airline__iata"],
        )[0]

        destination = Airport.objects.get_or_create(iata=attrs["destination__iata"])[0]

        origin = Airport.objects.get_or_create(
            iata=attrs["origin__iata"],
        )[0]

        trip = Trip.objects.get_or_create(
            name=attrs["trip__name"],
            start=attrs["trip__start"],
        )[0]

        DjangoFlight.objects.get(
            pk=self.pk,
        ).update(
            **{
                **{
                    k: v
                    for k, v in attrs.items()
                    if k
                    not in [
                        "airline__iata",
                        "destination__iata",
                        "origin__iata",
                        "trip__name",
                        "trip__start",
                    ]
                },
                "airline": airline,
                "destination": destination,
                "origin": origin,
                "trip": trip,
            },
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Flight":
        DjangoFlight.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
