from django.apps import AppConfig
from django.conf import settings

from illallangi.django.data.signals import ready_for_models
from illallangi.mastodon.adapters import MastodonAdapter


def add_model(
    **_kwargs: dict[str, object],
) -> None:
    from illallangi.django.data.models import Model, Synchronize

    Model.objects.create(
        description="Each status is a step towards discovering new horizons, embracing diverse cultures, and enriching your soul.",
        icon="mastodon/statuses.png",
        model="illallangi.data.mastodon.models.Status",
        plural="Statuses",
        singular="Status",
        url="status_list",
    )

    Synchronize.objects.create(
        callable="illallangi.data.mastodon.apps.synchronize",
    )


class MastodonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.mastodon"

    def ready(
        self,
    ) -> None:
        ready_for_models.connect(
            add_model,
        )


def synchronize() -> None:
    from illallangi.data.mastodon.adapters import (
        MastodonAdapter as DjangoAdapter,
    )

    src = MastodonAdapter(
        **settings.MASTODON,
    )
    dst = DjangoAdapter()

    src.load()
    dst.load()

    src.sync_to(dst)
