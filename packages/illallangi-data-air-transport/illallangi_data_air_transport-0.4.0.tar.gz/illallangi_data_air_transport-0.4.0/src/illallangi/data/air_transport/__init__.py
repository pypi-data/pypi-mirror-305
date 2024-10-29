import djp
from django.urls import URLPattern, re_path

from illallangi.data.air_transport import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.air_transport",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.air_transport import views

    return [
        re_path(
            r"^airlines/(?P<airline__slug>[\w\d-]+)/flights/$",
            views.flight_list,
            name="flight_list",
        ),
        re_path(
            r"^airports/(?P<airport__slug>[\w\d-]+)/flights/$",
            views.flight_list,
            name="flight_list",
        ),
        re_path(
            r"^flights/$",
            views.flight_list,
            name="flight_list",
        ),
        re_path(
            r"^flights/(?P<departure__year>[0-9]{4})/$",
            views.flight_list,
            name="flight_year",
        ),
        re_path(
            r"^flights/(?P<departure__year>[0-9]{4})/(?P<departure__month>[0-9]{2})/$",
            views.flight_list,
            name="flight_month",
        ),
        re_path(
            r"^flights/(?P<departure__year>[0-9]{4})/(?P<departure__month>[0-9]{2})/(?P<departure__day>[0-9]{2})/$",
            views.flight_list,
            name="flight_day",
        ),
        re_path(
            r"^flights/(?P<departure__year>[0-9]{4})/(?P<departure__month>[0-9]{2})/(?P<departure__day>[0-9]{2})/(?P<slug>[\w\d-]+)/$",
            views.flight_detail,
            name="flight_detail",
        ),
        re_path(
            r"^trips/$",
            views.trip_list,
            name="trip_list",
        ),
        re_path(
            r"^trips/(?P<start__year>[0-9]{4})/$",
            views.trip_list,
            name="trip_year",
        ),
        re_path(
            r"^trips/(?P<start__year>[0-9]{4})/(?P<start__month>[0-9]{2})/$",
            views.trip_list,
            name="trip_month",
        ),
        re_path(
            r"^trips/(?P<start__year>[0-9]{4})/(?P<start__month>[0-9]{2})/(?P<start__day>[0-9]{2})/$",
            views.trip_list,
            name="trip_day",
        ),
        re_path(
            r"^trips/(?P<start__year>[0-9]{4})/(?P<start__month>[0-9]{2})/(?P<start__day>[0-9]{2})/(?P<slug>[\w\d-]+)/$",
            views.trip_detail,
            name="trip_detail",
        ),
        re_path(
            r"^trips/(?P<trip__start__year>[0-9]{4})/(?P<trip__start__month>[0-9]{2})/(?P<trip__start__day>[0-9]{2})/(?P<trip__slug>[\w\d-]+)/flights/$",
            views.flight_list,
            name="flight_list",
        ),
    ]
