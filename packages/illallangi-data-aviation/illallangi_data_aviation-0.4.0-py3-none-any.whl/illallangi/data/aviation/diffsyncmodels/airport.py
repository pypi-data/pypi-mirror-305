import diffsync

from illallangi.data.aviation.models import Airport as ModelAirport


class Airport(
    diffsync.DiffSyncModel,
):
    _modelname = "Airport"
    _identifiers = ("iata",)
    _attributes = (
        "icao",
        "label",
    )

    pk: int

    iata: str

    icao: str | None
    label: str | None

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Airport":
        obj = ModelAirport.objects.update_or_create(
            iata=ids["iata"],
            defaults={
                "label": attrs["label"],
                "icao": attrs["icao"],
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
    ) -> "Airport":
        ModelAirport.objects.filter(
            pk=self.pk,
        ).update(
            **attrs,
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Airport":
        ModelAirport.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
