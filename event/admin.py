from django.contrib import admin
from .models import Event, Venue

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'price', 'time', 'maximum_people']
    list_filter = ['location', 'maximum_people']
    search_fields = ['name', 'location', 'hosts']
    list_per_page = 20

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity', 'price_per_hour', 'available']
    list_filter = ['location', 'available']
    search_fields = ['name', 'location']
    list_editable = ['available']
    list_per_page = 20

admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)
