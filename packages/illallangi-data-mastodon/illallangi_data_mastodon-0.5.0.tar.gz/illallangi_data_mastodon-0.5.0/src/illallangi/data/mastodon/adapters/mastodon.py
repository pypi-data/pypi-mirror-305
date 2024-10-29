from typing import ClassVar

import diffsync
from yarl import URL

from illallangi.data.mastodon.diffsyncmodels import Status
from illallangi.data.mastodon.models import Status as DjangoStatus


class MastodonAdapter(diffsync.Adapter):
    Status = Status

    top_level: ClassVar = [
        "Status",
    ]

    type = "django_mastodon"

    def load(
        self,
    ) -> None:
        for obj in DjangoStatus.objects.all():
            self.add(
                Status(
                    pk=obj.pk,
                    url=URL(obj.url),
                    content=obj.content,
                    datetime=obj.datetime,
                ),
            )
