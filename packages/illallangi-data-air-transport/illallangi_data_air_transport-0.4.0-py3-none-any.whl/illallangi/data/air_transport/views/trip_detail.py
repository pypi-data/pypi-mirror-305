import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.air_transport.models import Trip


@require_GET
def trip_detail(
    request: HttpRequest,
    start__year: str,
    start__month: str,
    start__day: str,
    slug: str,
) -> render:
    objects = Trip.objects.filter(
        start__year=start__year,
        start__month=start__month,
        start__day=start__day,
        slug=slug,
    )

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple trips found",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "air_transport/trip_detail.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Trips",
                        "url": reverse(
                            "trip_list",
                        ),
                    },
                    {
                        "title": obj.start.year,
                        "url": reverse(
                            "trip_year",
                            kwargs={
                                "start__year": str(obj.start.year).zfill(4),
                            },
                        ),
                    },
                    {
                        "title": calendar.month_name[obj.start.month],
                        "url": reverse(
                            "trip_month",
                            kwargs={
                                "start__year": str(obj.start.year).zfill(4),
                                "start__month": str(obj.start.month).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": ordinal(start__day),
                        "url": reverse(
                            "trip_day",
                            kwargs={
                                "start__year": str(obj.start.year).zfill(4),
                                "start__month": str(obj.start.month).zfill(2),
                                "start__day": str(obj.start.day).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": str(obj),
                        "url": reverse(
                            "trip_detail",
                            kwargs={
                                "start__year": str(obj.start.year).zfill(4),
                                "start__month": str(obj.start.month).zfill(2),
                                "start__day": str(obj.start.day).zfill(2),
                                "slug": slug,
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
                                "trip__start__year": str(obj.start.year).zfill(4),
                                "trip__start__month": str(obj.start.month).zfill(2),
                                "trip__start__day": str(obj.start.day).zfill(2),
                                "trip__slug": slug,
                            },
                        ),
                        "title": related_object.related_model._meta.verbose_name_plural.title(),  # noqa: SLF001
                        "count": related_object.related_model.objects.filter(
                            models.Q(trip=obj)
                        ).count(),
                    }
                    for related_object in obj._meta.related_objects  # noqa: SLF001
                }.values(),
            },
        )

    return HttpResponse(
        status=400,
        content="Trip not found",
    )
