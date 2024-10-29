import djp
from django.urls import URLPattern, re_path

from illallangi.data.fitness import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.fitness",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.fitness import views

    return [
        re_path(
            r"^swims/$",
            views.swim_list,
            name="swim_list",
        ),
        re_path(
            r"^swims/(?P<date__year>[0-9]{4})/$",
            views.swim_list,
            name="swim_year",
        ),
        re_path(
            r"^swims/(?P<date__year>[0-9]{4})/(?P<date__month>[0-9]{2})/$",
            views.swim_list,
            name="swim_month",
        ),
        re_path(
            r"^swims/(?P<date__year>[0-9]{4})/(?P<date__month>[0-9]{2})/(?P<date__day>[0-9]{2})/$",
            views.swim_list,
            name="swim_day",
        ),
        re_path(
            r"^swims/(?P<date__year>[0-9]{4})/(?P<date__month>[0-9]{2})/(?P<date__day>[0-9]{2})/(?P<slug>[\w\d-]+)/$",
            views.swim_detail,
            name="swim_detail",
        ),
    ]
