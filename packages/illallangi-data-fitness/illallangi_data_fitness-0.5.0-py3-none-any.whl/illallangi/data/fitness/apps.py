from django.apps import AppConfig
from django.conf import settings

from illallangi.django.data.signals import ready_for_models
from illallangi.mastodon.adapters import FitnessAdapter as MastodonAdapter


def add_model(
    **_kwargs: dict[str, object],
) -> None:
    from illallangi.django.data.models import Model, Synchronize

    Model.objects.create(
        description="Swimming is a fantastic way to improve overall fitness and well-being.",
        icon="fitness/swims.png",
        model="illallangi.data.fitness.models.swim.Swim",
        plural="Swims",
        singular="Swim",
        url="swim_list",
    )

    Synchronize.objects.create(
        callable="illallangi.data.fitness.apps.synchronize",
    )


class MastodonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.fitness"

    def ready(
        self,
    ) -> None:
        ready_for_models.connect(
            add_model,
        )


def synchronize() -> None:
    from illallangi.data.fitness.adapters import (
        FitnessAdapter as DjangoAdapter,
    )

    src = MastodonAdapter(
        **settings.MASTODON,
    )
    dst = DjangoAdapter()

    src.load()
    dst.load()

    src.sync_to(dst)
