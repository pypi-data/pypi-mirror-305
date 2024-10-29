import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.mastodon.models import Status


@require_GET
def status_list(
    request: HttpRequest,
    datetime__year: str | None = None,
    datetime__month: str | None = None,
    datetime__day: str | None = None,
) -> render:
    objects = Status.objects.all()
    breadcrumbs = []

    if not False:
        breadcrumbs.append(
            {
                "title": "Statuses",
                "url": reverse(
                    "status_list",
                ),
            },
        )

    if datetime__year:
        objects = objects.filter(
            Q(datetime__year=datetime__year),
        )
        breadcrumbs.append(
            {
                "title": datetime__year,
                "url": reverse(
                    "status_year",
                    kwargs={
                        "datetime__year": datetime__year,
                    },
                ),
            },
        )

    if datetime__month:
        objects = objects.filter(
            Q(datetime__month=datetime__month),
        )
        breadcrumbs.append(
            {
                "title": calendar.month_name[int(datetime__month)],
                "url": reverse(
                    "status_month",
                    kwargs={
                        "datetime__year": datetime__year,
                        "datetime__month": datetime__month,
                    },
                ),
            },
        )

    if datetime__day:
        objects = objects.filter(
            Q(datetime__day=datetime__day),
        )
        breadcrumbs.append(
            {
                "title": ordinal(datetime__day),
                "url": reverse(
                    "status_day",
                    kwargs={
                        "datetime__year": datetime__year,
                        "datetime__month": datetime__month,
                        "datetime__day": datetime__day,
                    },
                ),
            },
        )

    if objects.count() == 1:
        return redirect(
            reverse(
                "status_detail",
                kwargs={
                    "datetime__year": str(objects.first().datetime.year).zfill(4),
                    "datetime__month": str(objects.first().datetime.month).zfill(2),
                    "datetime__day": str(objects.first().datetime.day).zfill(2),
                    "slug": objects.first().slug,
                },
            ),
        )

    return render(
        request,
        "mastodon/status_list.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by(
                    "datetime",
                ),
                per_page=10,
            ).get_page(
                request.GET.get("page", 1),
            ),
            "breadcrumbs": breadcrumbs,
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "href": request.build_absolute_uri(
                        request.get_full_path(),
                    ),
                },
            ],
        },
    )
