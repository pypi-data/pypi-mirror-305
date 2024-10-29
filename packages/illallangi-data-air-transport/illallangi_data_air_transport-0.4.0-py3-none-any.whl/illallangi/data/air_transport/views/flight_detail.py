import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.air_transport.models import Flight


@require_GET
def flight_detail(
    request: HttpRequest,
    departure__year: str,
    departure__month: str,
    departure__day: str,
    slug: str,
) -> render:
    objects = Flight.objects.filter(
        departure__year=departure__year,
        departure__month=departure__month,
        departure__day=departure__day,
        slug=slug,
    )

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple flights found",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "air_transport/flight_detail.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Flights",
                        "url": reverse(
                            "flight_list",
                        ),
                    },
                    {
                        "title": obj.departure.year,
                        "url": reverse(
                            "flight_year",
                            kwargs={
                                "departure__year": str(obj.departure.year).zfill(4),
                            },
                        ),
                    },
                    {
                        "title": calendar.month_name[obj.departure.month],
                        "url": reverse(
                            "flight_month",
                            kwargs={
                                "departure__year": str(obj.departure.year).zfill(4),
                                "departure__month": str(obj.departure.month).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": ordinal(departure__day),
                        "url": reverse(
                            "flight_day",
                            kwargs={
                                "departure__year": str(obj.departure.year).zfill(4),
                                "departure__month": str(obj.departure.month).zfill(2),
                                "departure__day": str(obj.departure.day).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": str(obj),
                        "url": reverse(
                            "flight_detail",
                            kwargs={
                                "departure__year": str(obj.departure.year).zfill(4),
                                "departure__month": str(obj.departure.month).zfill(2),
                                "departure__day": str(obj.departure.day).zfill(2),
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
                                "flight__departure__year": departure__year,
                                "flight__departure__month": departure__month,
                                "flight__departure__day": departure__day,
                                "flight__slug": slug,
                            },
                        ),
                        "title": related_object.related_model._meta.verbose_name_plural.title(),  # noqa: SLF001
                        "count": related_object.related_model.objects.filter(
                            models.Q(airline=obj)
                        ).count(),
                    }
                    for related_object in obj._meta.related_objects  # noqa: SLF001
                }.values(),
            },
        )

    return HttpResponse(
        status=400,
        content="Flight not found",
    )
