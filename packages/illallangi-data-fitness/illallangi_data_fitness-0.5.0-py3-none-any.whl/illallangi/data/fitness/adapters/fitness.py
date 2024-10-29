from typing import ClassVar

import diffsync
from yarl import URL

from illallangi.data.fitness.diffsyncmodels import Swim
from illallangi.data.fitness.models import Swim as DjangoSwim


class FitnessAdapter(diffsync.Adapter):
    Swim = Swim

    top_level: ClassVar = [
        "Swim",
    ]

    type = "data_fitness"

    def load(
        self,
    ) -> None:
        for obj in DjangoSwim.objects.all():
            self.add(
                Swim(
                    pk=obj.pk,
                    url=URL(obj.url),
                    date=obj.date,
                    distance=obj.distance,
                    laps=obj.laps,
                ),
            )
