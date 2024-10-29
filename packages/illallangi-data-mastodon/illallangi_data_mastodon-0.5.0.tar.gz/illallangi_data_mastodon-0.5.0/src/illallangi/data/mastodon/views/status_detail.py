import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.mastodon.models import Status


@require_GET
def status_detail(
    request: HttpRequest,
    datetime__day: str,
    datetime__month: str,
    datetime__year: str,
    slug: str,
) -> render:
    objects = Status.objects.filter(
        datetime__year=datetime__year,
        datetime__month=datetime__month,
        datetime__day=datetime__day,
        slug=slug,
    )

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple statuses found",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "mastodon/status_detail.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Statuses",
                        "url": reverse(
                            "status_list",
                        ),
                    },
                    {
                        "title": obj.datetime.year,
                        "url": reverse(
                            "status_year",
                            kwargs={
                                "datetime__year": str(obj.datetime.year).zfill(4),
                            },
                        ),
                    },
                    {
                        "title": calendar.month_name[obj.datetime.month],
                        "url": reverse(
                            "status_month",
                            kwargs={
                                "datetime__year": str(obj.datetime.year).zfill(4),
                                "datetime__month": str(obj.datetime.month).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": ordinal(obj.datetime.day),
                        "url": reverse(
                            "status_day",
                            kwargs={
                                "datetime__year": str(obj.datetime.year).zfill(4),
                                "datetime__month": str(obj.datetime.month).zfill(2),
                                "datetime__day": str(obj.datetime.day).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": str(obj),
                        "url": reverse(
                            "status_detail",
                            kwargs={
                                "datetime__year": str(obj.datetime.year).zfill(4),
                                "datetime__month": str(obj.datetime.month).zfill(2),
                                "datetime__day": str(obj.datetime.day).zfill(2),
                                "slug": obj.slug,
                            },
                        ),
                    },
                ],
                "links": [
                    {
                        "rel": "alternate",
                        "type": "text/html",
                        "href": request.build_absolute_uri(
                            request.get_full_path(),
                        ),
                    },
                ],
                "related_objects": {
                    related_object.related_model._meta.verbose_name.title(): {  # noqa: SLF001
                        "href": reverse(
                            f"{related_object.related_model._meta.verbose_name.lower()}_list",  # noqa: SLF001
                            kwargs={
                                "status__datetime__year": str(obj.datetime.year).zfill(
                                    4
                                ),
                                "status__datetime__month": str(
                                    obj.datetime.month
                                ).zfill(2),
                                "status__datetime__day": str(obj.datetime.day).zfill(2),
                                "status__slug": obj.slug,
                            },
                        ),
                        "title": related_object.related_model._meta.verbose_name_plural.title(),  # noqa: SLF001
                        "count": related_object.related_model.objects.filter(
                            models.Q(alliance=obj)
                        ).count(),
                    }
                    for related_object in obj._meta.related_objects  # noqa: SLF001
                }.values(),
            },
        )

    return HttpResponse(
        status=400,
        content="Status not found",
    )
