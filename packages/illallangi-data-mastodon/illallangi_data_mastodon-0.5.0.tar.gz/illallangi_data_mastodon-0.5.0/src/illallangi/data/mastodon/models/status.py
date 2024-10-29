from autoslug import AutoSlugField
from django.db import models


class Status(
    models.Model,
):
    # Surrogate Keys

    id = models.AutoField(
        primary_key=True,
    )

    slug = AutoSlugField(
        populate_from="get_slug",
        unique_with=(
            "datetime__year",
            "datetime__month",
            "datetime__day",
        ),
    )

    # Natural Keys

    url = models.URLField(
        blank=False,
        null=False,
        unique=True,
    )

    # Fields

    content = models.TextField(
        blank=False,
        null=False,
    )

    datetime = models.DateTimeField(
        blank=False,
        null=False,
    )

    # Methods

    def __str__(
        self,
    ) -> str:
        return f"Status {self.id}"

    def get_slug(
        self,
    ) -> str:
        return "post"
