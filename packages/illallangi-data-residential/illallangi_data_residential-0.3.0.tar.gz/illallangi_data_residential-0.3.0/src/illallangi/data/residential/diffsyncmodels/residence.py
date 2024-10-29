import diffsync
from partial_date import PartialDate

from illallangi.data.residential.models.residence import (
    Residence as ModelResidence,
)


class Residence(diffsync.DiffSyncModel):
    _modelname = "Residence"
    _identifiers = ("label",)
    _attributes = (
        "country",
        "finish",
        "locality",
        "open_location_code",
        "postal_code",
        "region",
        "start",
        "street",
    )

    pk: int

    label: str

    country: str
    finish: PartialDate | None
    locality: str
    open_location_code: str
    postal_code: str
    region: str
    start: PartialDate | None
    street: str

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Residence":
        obj = ModelResidence.objects.update_or_create(
            label=ids["label"],
            defaults={
                "country": attrs["country"],
                "finish": attrs["finish"],
                "locality": attrs["locality"],
                "open_location_code": attrs["open_location_code"],
                "postal_code": attrs["postal_code"],
                "region": attrs["region"],
                "start": attrs["start"],
                "street": attrs["street"],
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
    ) -> "Residence":
        ModelResidence.objects.filter(
            pk=self.pk,
        ).update(
            **attrs,
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Residence":
        ModelResidence.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
