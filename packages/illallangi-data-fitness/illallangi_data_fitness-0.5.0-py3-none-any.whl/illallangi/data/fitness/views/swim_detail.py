import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.fitness.models import Swim


@require_GET
def swim_detail(
    request: HttpRequest,
    date__day: str,
    date__month: str,
    date__year: str,
    slug: str,
) -> render:
    objects = Swim.objects.filter(
        date__year=date__year,
        date__month=date__month,
        date__day=date__day,
        slug=slug,
    )

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple swims found",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "fitness/swim_detail.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Swims",
                        "url": reverse(
                            "swim_list",
                        ),
                    },
                    {
                        "title": obj.date.year,
                        "url": reverse(
                            "swim_year",
                            kwargs={
                                "date__year": str(obj.date.year).zfill(4),
                            },
                        ),
                    },
                    {
                        "title": calendar.month_name[obj.date.month],
                        "url": reverse(
                            "swim_month",
                            kwargs={
                                "date__year": str(obj.date.year).zfill(4),
                                "date__month": str(obj.date.month).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": ordinal(obj.date.day),
                        "url": reverse(
                            "swim_day",
                            kwargs={
                                "date__year": str(obj.date.year).zfill(4),
                                "date__month": str(obj.date.month).zfill(2),
                                "date__day": str(obj.date.day).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": str(obj),
                        "url": reverse(
                            "swim_detail",
                            kwargs={
                                "date__year": str(obj.date.year).zfill(4),
                                "date__month": str(obj.date.month).zfill(2),
                                "date__day": str(obj.date.day).zfill(2),
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
                                "swim__date__year": str(obj.date.year).zfill(4),
                                "swim__date__month": str(obj.date.month).zfill(2),
                                "swim__date__day": str(obj.date.day).zfill(2),
                                "swim__slug": obj.slug,
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
        content="Swim not found",
    )
