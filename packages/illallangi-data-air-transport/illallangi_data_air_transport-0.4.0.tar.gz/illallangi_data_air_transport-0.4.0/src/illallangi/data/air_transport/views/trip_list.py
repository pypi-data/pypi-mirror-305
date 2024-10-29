import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.air_transport.models import Flight, Trip


@require_GET
def trip_list(  # noqa: PLR0913
    request: HttpRequest,
    flight__departure__year: str | None = None,
    flight__departure__month: str | None = None,
    flight__departure__day: str | None = None,
    flight__slug: str | None = None,
    start__year: str | None = None,
    start__month: str | None = None,
    start__day: str | None = None,
) -> render:
    objects = Trip.objects.all()
    breadcrumbs = []

    if (
        flight__departure__year
        and flight__departure__month
        and flight__departure__day
        and flight__slug
    ):
        flight = Flight.objects.get(
            Q(departure__year=flight__departure__year)
            & Q(departure__month=flight__departure__month)
            & Q(departure__day=flight__departure__day)
            & Q(slug=flight__slug),
        )
        objects = objects.filter(
            Q(flight=flight),
        )
        breadcrumbs.append(
            {
                "title": "Flights",
                "url": reverse(
                    "flight_list",
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": flight.departure.year,
                "url": reverse(
                    "flight_year",
                    kwargs={
                        "flight__departure__year": str(flight.departure.year).zfill(4),
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": calendar.month_name[int(flight__departure__month)],
                "url": reverse(
                    "flight_month",
                    kwargs={
                        "flight__departure__year": str(flight.departure.year).zfill(2),
                        "flight__departure__month": str(flight.departure.month).zfill(
                            2
                        ),
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": ordinal(flight__departure__day),
                "url": reverse(
                    "flight_day",
                    kwargs={
                        "flight__departure__year": str(flight.departure.year).zfill(2),
                        "flight__departure__month": str(flight.departure.month).zfill(
                            2
                        ),
                        "flight__departure__day": str(flight.departure.day).zfill(2),
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": str(flight),
                "url": reverse(
                    "flight_detail",
                    kwargs={
                        "departure__year": str(flight.departure.year).zfill(2),
                        "departure__month": str(flight.departure.month).zfill(2),
                        "departure__day": str(flight.departure.day).zfill(2),
                        "slug": flight__slug,
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": "Trips",
                "url": reverse(
                    "trip_list",
                    kwargs={
                        "departure__year": str(flight.departure.year).zfill(2),
                        "departure__month": str(flight.departure.month).zfill(2),
                        "departure__day": str(flight.departure.day).zfill(2),
                        "slug": flight__slug,
                    },
                ),
            },
        )

    if (
        not flight__departure__year
        and not flight__departure__month
        and not flight__departure__day
        and not flight__slug
    ):
        breadcrumbs.append(
            {
                "title": "Trips",
                "url": reverse(
                    "trip_list",
                ),
            },
        )

    if start__year:
        objects = objects.filter(
            Q(start__year=start__year),
        )
        breadcrumbs.append(
            {
                "title": start__year,
                "url": reverse(
                    "trip_year",
                    kwargs={
                        "start__year": start__year,
                    },
                ),
            },
        )

    if start__month:
        objects = objects.filter(
            Q(start__month=start__month),
        )
        breadcrumbs.append(
            {
                "title": calendar.month_name[int(start__month)],
                "url": reverse(
                    "trip_month",
                    kwargs={
                        "start__year": start__year,
                        "start__month": start__month,
                    },
                ),
            },
        )

    if start__day:
        objects = objects.filter(
            Q(start__day=start__day),
        )
        breadcrumbs.append(
            {
                "title": ordinal(start__day),
                "url": reverse(
                    "trip_day",
                    kwargs={
                        "start__year": start__year,
                        "start__month": start__month,
                        "start__day": start__day,
                    },
                ),
            },
        )

    if objects.count() == 1:
        return redirect(
            reverse(
                "trip_detail",
                kwargs={
                    "start__year": str(objects.first().start.year).zfill(4),
                    "start__month": str(objects.first().start.month).zfill(2),
                    "start__day": str(objects.first().start.day).zfill(2),
                    "slug": objects.first().slug,
                },
            ),
        )

    return render(
        request,
        "air_transport/trip_list.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by(
                    "start",
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
