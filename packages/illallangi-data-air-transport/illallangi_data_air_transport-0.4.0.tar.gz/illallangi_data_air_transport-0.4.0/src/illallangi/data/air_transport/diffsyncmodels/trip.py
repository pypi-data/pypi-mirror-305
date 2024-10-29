from datetime import datetime

import diffsync

from illallangi.data.air_transport.models import Trip as DjangoTrip


class Trip(
    diffsync.DiffSyncModel,
):
    _modelname = "Trip"
    _identifiers = (
        "name",
        "start",
    )
    _attributes = (
        "end",
        "open_location_code",
    )

    pk: int

    name: str
    start: datetime

    end: datetime | None
    open_location_code: str | None

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Trip":
        obj = DjangoTrip.objects.update_or_create(
            **ids,
            defaults=attrs,
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
    ) -> "Trip":
        DjangoTrip.objects.filter(
            pk=self.pk,
        ).update(
            **attrs,
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Trip":
        DjangoTrip.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
