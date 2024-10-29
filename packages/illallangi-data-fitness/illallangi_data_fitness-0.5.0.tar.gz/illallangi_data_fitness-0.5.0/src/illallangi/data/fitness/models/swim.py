from autoslug import AutoSlugField
from django.db import models


class Swim(
    models.Model,
):
    # Surrogate Keys

    id = models.AutoField(
        primary_key=True,
    )

    slug = AutoSlugField(
        populate_from="get_slug",
        unique_with=(
            "date__year",
            "date__month",
            "date__day",
        ),
    )

    # Natural Keys

    url = models.URLField(
        blank=False,
        null=False,
        unique=True,
    )

    # Fields

    date = models.DateField(
        blank=False,
        null=False,
    )

    distance = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    laps = models.FloatField(
        blank=False,
        null=False,
    )

    # Methods

    def __str__(
        self,
    ) -> str:
        return f"{self.distance}m Swim"

    def get_slug(
        self,
    ) -> str:
        return "swim"
