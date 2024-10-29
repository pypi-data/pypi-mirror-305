import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.fitness.models import Swim


@require_GET
def swim_list(
    request: HttpRequest,
    date__year: str | None = None,
    date__month: str | None = None,
    date__day: str | None = None,
) -> render:
    objects = Swim.objects.all()
    breadcrumbs = []

    if not False:
        breadcrumbs.append(
            {
                "title": "Swims",
                "url": reverse(
                    "swim_list",
                ),
            },
        )

    if date__year:
        objects = objects.filter(
            Q(date__year=date__year),
        )
        breadcrumbs.append(
            {
                "title": date__year,
                "url": reverse(
                    "swim_year",
                    kwargs={
                        "date__year": date__year,
                    },
                ),
            },
        )

    if date__month:
        objects = objects.filter(
            Q(date__month=date__month),
        )
        breadcrumbs.append(
            {
                "title": calendar.month_name[int(date__month)],
                "url": reverse(
                    "swim_month",
                    kwargs={
                        "date__year": date__year,
                        "date__month": date__month,
                    },
                ),
            },
        )

    if date__day:
        objects = objects.filter(
            Q(date__day=date__day),
        )
        breadcrumbs.append(
            {
                "title": ordinal(date__day),
                "url": reverse(
                    "swim_day",
                    kwargs={
                        "date__year": date__year,
                        "date__month": date__month,
                        "date__day": date__day,
                    },
                ),
            },
        )

    if objects.count() == 1:
        return redirect(
            reverse(
                "swim_detail",
                kwargs={
                    "date__year": str(objects.first().date.year).zfill(4),
                    "date__month": str(objects.first().date.month).zfill(2),
                    "date__day": str(objects.first().date.day).zfill(2),
                    "slug": objects.first().slug,
                },
            ),
        )

    return render(
        request,
        "fitness/swim_list.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by(
                    "date",
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
