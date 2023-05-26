from django.contrib import admin

from .models import BookedOneWay, BookedRoundTrip, OneWayFlight, RoundTripFlight

# models registered in admin

admin.site.register(OneWayFlight)
admin.site.register(RoundTripFlight)
admin.site.register(BookedRoundTrip)
admin.site.register(BookedOneWay)
