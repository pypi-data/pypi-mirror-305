import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.air_transport.models import Flight, Trip
from illallangi.data.aviation.models import Airline, Airport


@require_GET
def flight_list(  # noqa: PLR0913
    request: HttpRequest,
    trip__start__year: str | None = None,
    trip__start__month: str | None = None,
    trip__start__day: str | None = None,
    trip__slug: str | None = None,
    airline__slug: str | None = None,
    airport__slug: str | None = None,
    departure__year: str | None = None,
    departure__month: str | None = None,
    departure__day: str | None = None,
) -> render:
    objects = Flight.objects.all()
    breadcrumbs = []

    if trip__start__year and trip__start__month and trip__start__day and trip__slug:
        trip = Trip.objects.get(
            Q(start__year=trip__start__year)
            & Q(start__month=trip__start__month)
            & Q(start__day=trip__start__day)
            & Q(slug=trip__slug),
        )
        objects = objects.filter(
            Q(trip=trip),
        )
        breadcrumbs.append(
            {
                "title": "Trips",
                "url": reverse(
                    "trip_list",
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": trip.start.year,
                "url": reverse(
                    "trip_year",
                    kwargs={
                        "start__year": str(trip.start.year).zfill(4),
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": calendar.month_name[int(trip.start.month)],
                "url": reverse(
                    "trip_month",
                    kwargs={
                        "start__year": str(trip.start.year).zfill(4),
                        "start__month": str(trip.start.month).zfill(2),
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": ordinal(trip.start.day),
                "url": reverse(
                    "trip_day",
                    kwargs={
                        "start__year": str(trip.start.year).zfill(4),
                        "start__month": str(trip.start.month).zfill(2),
                        "start__day": str(trip.start.day).zfill(2),
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": str(trip),
                "url": reverse(
                    "trip_detail",
                    kwargs={
                        "start__year": str(trip.start.year).zfill(4),
                        "start__month": str(trip.start.month).zfill(2),
                        "start__day": str(trip.start.day).zfill(2),
                        "slug": trip.slug,
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": "Flights",
                "url": reverse(
                    "flight_list",
                    kwargs={
                        "trip__start__year": str(trip.start.year).zfill(4),
                        "trip__start__month": str(trip.start.month).zfill(2),
                        "trip__start__day": str(trip.start.day).zfill(2),
                        "trip__slug": trip.slug,
                    },
                ),
            },
        )

    if airline__slug:
        airline = Airline.objects.get(
            Q(slug=airline__slug),
        )
        objects = objects.filter(
            Q(airline=airline),
        )
        breadcrumbs.append(
            {
                "title": "Airlines",
                "url": reverse(
                    "airline_list",
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": str(airline),
                "url": reverse(
                    "airline_detail",
                    kwargs={
                        "slug": airline.slug,
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": "Flights",
                "url": reverse(
                    "flight_list",
                    kwargs={
                        "airline__slug": airline.slug,
                    },
                ),
            },
        )

    if airport__slug:
        airport = Airport.objects.get(
            Q(slug=airport__slug),
        )
        objects = objects.filter(
            Q(origin=airport) | Q(destination=airport),
        )
        breadcrumbs.append(
            {
                "title": "Airports",
                "url": reverse(
                    "airport_list",
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": str(airport),
                "url": reverse(
                    "airport_detail",
                    kwargs={
                        "slug": airport.slug,
                    },
                ),
            },
        )
        breadcrumbs.append(
            {
                "title": "Flights",
                "url": reverse(
                    "flight_list",
                    kwargs={
                        "airport__slug": airport.slug,
                    },
                ),
            },
        )

    if (
        not trip__start__year
        and not trip__start__month
        and not trip__start__day
        and not trip__slug
        and not airline__slug
        and not airport__slug
    ):
        breadcrumbs.append(
            {
                "title": "Flights",
                "url": reverse(
                    "flight_list",
                ),
            },
        )

    if departure__year:
        objects = objects.filter(
            Q(departure__year=departure__year),
        )
        breadcrumbs.append(
            {
                "title": departure__year,
                "url": reverse(
                    "flight_year",
                    kwargs={
                        "departure__year": departure__year,
                    },
                ),
            },
        )

    if departure__month:
        objects = objects.filter(
            Q(departure__month=departure__month),
        )
        breadcrumbs.append(
            {
                "title": calendar.month_name[int(departure__month)],
                "url": reverse(
                    "flight_month",
                    kwargs={
                        "departure__year": departure__year,
                        "departure__month": departure__month,
                    },
                ),
            },
        )

    if departure__day:
        objects = objects.filter(
            Q(departure__day=departure__day),
        )
        breadcrumbs.append(
            {
                "title": ordinal(departure__day),
                "url": reverse(
                    "flight_day",
                    kwargs={
                        "departure__year": departure__year,
                        "departure__month": departure__month,
                        "departure__day": departure__day,
                    },
                ),
            },
        )

    if objects.count() == 1:
        return redirect(
            reverse(
                "flight_detail",
                kwargs={
                    "departure__year": str(objects.first().departure.year).zfill(4),
                    "departure__month": str(objects.first().departure.month).zfill(2),
                    "departure__day": str(objects.first().departure.day).zfill(2),
                    "slug": objects.first().slug,
                },
            ),
        )

    return render(
        request,
        "air_transport/flight_list.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by(
                    "departure",
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
