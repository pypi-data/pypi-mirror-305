from django.apps import AppConfig
from django.conf import settings

from illallangi.django.data.signals import ready_for_models
from illallangi.tripit.adapters import AirTransportAdapter as TripItAdapter


def add_model(
    **_kwargs: dict[str, object],
) -> None:
    from illallangi.django.data.models import Model, Synchronize

    Model.objects.create(
        description="Every leg of a journey, no matter how long or short, brings you closer to your destination.",
        icon="air_transport/flights.jpg",
        model="illallangi.data.air_transport.models.Flight",
        plural="Flights",
        singular="Flight",
        url="flight_list",
    )
    Model.objects.create(
        description="Each trip is a step towards discovering new horizons, embracing diverse cultures, and enriching your soul.",
        icon="air_transport/trips.jpg",
        model="illallangi.data.air_transport.models.Trip",
        plural="Trips",
        singular="Trip",
        url="trip_list",
    )

    Synchronize.objects.create(
        callable="illallangi.data.air_transport.apps.synchronize",
        before=["illallangi.data.aviation.apps.synchronize"],
    )


class AirTransportConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.air_transport"

    def ready(
        self,
    ) -> None:
        ready_for_models.connect(
            add_model,
        )


def synchronize() -> None:
    from illallangi.data.air_transport.adapters import (
        AirTransportAdapter as DjangoAdapter,
    )

    src = TripItAdapter(
        **settings.TRIPIT,
    )
    dst = DjangoAdapter()

    src.load(
        **settings.AIR_TRANSPORT,
    )
    dst.load()

    src.sync_to(dst)
