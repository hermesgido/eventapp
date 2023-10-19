from django.contrib import admin
from .models import Event, EventBooking, Venue, VenueBooking

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


class EventBookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'booking_date', 'booking_duration', 'is_approved')
    list_filter = ('is_approved', )
    actions = ['approve_selected_bookings']

    def approve_selected_bookings(self, request, queryset):
        # Custom action to approve selected bookings
        queryset.update(is_approved=True)

class VenueBookingAdmin(admin.ModelAdmin):
    list_display = ('venue', 'user', 'booking_date', 'booking_duration', 'is_approved')
    list_filter = ('is_approved', )
    actions = ['approve_selected_bookings']

    def approve_selected_bookings(self, request, queryset):
        # Custom action to approve selected bookings
        queryset.update(is_approved=True)

admin.site.register(EventBooking, EventBookingAdmin)
admin.site.register(VenueBooking, VenueBookingAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)


