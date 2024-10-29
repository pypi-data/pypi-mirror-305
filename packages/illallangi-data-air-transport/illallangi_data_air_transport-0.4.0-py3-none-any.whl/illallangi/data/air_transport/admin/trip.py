from django.contrib.admin import ModelAdmin, register

from illallangi.data.air_transport.models import Trip


@register(Trip)
class TripModelAdmin(ModelAdmin):
    pass
