from django.contrib import admin
from .models import Event, EventBooking, Venue, VenueBooking

class EventBookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'booking_date', 'booking_duration', 'is_approved', 'is_canceled')
    list_filter = ('is_approved', )
    actions = ['approve_selected_bookings']

    def approve_selected_bookings(self, request, queryset):
        # Custom action to approve selected bookings
        queryset.update(is_approved=True)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(event__user=request.user)
        return qs.filter(event__user=request.user)

class VenueBookingAdmin(admin.ModelAdmin):
    list_display = ('venue', 'user', 'booking_date', 'booking_duration', 'is_approved', 'is_canceled')
    list_filter = ('is_approved', )
    actions = ['approve_selected_bookings']

    def approve_selected_bookings(self, request, queryset):
        # Custom action to approve selected bookings
        queryset.update(is_approved=True)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(venue__user=request.user)

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity', 'price_per_hour', 'available']
    list_filter = ['location', 'available']
    search_fields = ['name', 'location']
    list_editable = ['available']
    list_per_page = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs.filter(user=request.user)



from django.utils.html import format_html

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'price', 'time', 'maximum_people', 'display_event_bookings']
    list_filter = ['location', 'maximum_people']
    search_fields = ['name', 'location', 'hosts']
    list_per_page = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs.filter(user=request.user)

    # Define a custom method to display a link to related event bookings
    def display_event_bookings(self, obj):
        url = f"/admin/event/eventbooking/?event__id__exact={obj.id}"
        return format_html('<a href="{}">View Bookings</a>', url)

    display_event_bookings.short_description = 'Event Bookings'

    # Set a link to the event's change page
    list_display_links = ['name', 'display_event_bookings']

admin.site.register(EventBooking, EventBookingAdmin)
admin.site.register(VenueBooking, VenueBookingAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)




