import djp
from django.urls import URLPattern, re_path

from illallangi.data.mastodon import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.mastodon",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.mastodon import views

    return [
        re_path(
            r"^statuses/$",
            views.status_list,
            name="status_list",
        ),
        re_path(
            r"^statuses/(?P<datetime__year>[0-9]{4})/$",
            views.status_list,
            name="status_year",
        ),
        re_path(
            r"^statuses/(?P<datetime__year>[0-9]{4})/(?P<datetime__month>[0-9]{2})/$",
            views.status_list,
            name="status_month",
        ),
        re_path(
            r"^statuses/(?P<datetime__year>[0-9]{4})/(?P<datetime__month>[0-9]{2})/(?P<datetime__day>[0-9]{2})/$",
            views.status_list,
            name="status_day",
        ),
        re_path(
            r"^statuses/(?P<datetime__year>[0-9]{4})/(?P<datetime__month>[0-9]{2})/(?P<datetime__day>[0-9]{2})/(?P<slug>[\w\d-]+)/$",
            views.status_detail,
            name="status_detail",
        ),
    ]
