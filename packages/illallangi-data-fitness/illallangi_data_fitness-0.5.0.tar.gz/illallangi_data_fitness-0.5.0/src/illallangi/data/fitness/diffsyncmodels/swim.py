from datetime import date

import diffsync
from yarl import URL

from illallangi.data.fitness.models.swim import Swim as ModelSwim


class Swim(
    diffsync.DiffSyncModel,
):
    _modelname = "Swim"
    _identifiers = ("url",)
    _attributes = (
        "date",
        "distance",
        "laps",
    )

    pk: int

    url: URL

    date: date
    distance: int
    laps: float

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Swim":
        obj = ModelSwim.objects.update_or_create(
            url=ids["url"],
            defaults={
                "date": attrs["date"],
                "distance": attrs["distance"],
                "laps": attrs["laps"],
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
    ) -> "Swim":
        ModelSwim.objects.filter(
            pk=self.pk,
        ).update(
            **attrs,
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Swim":
        ModelSwim.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
