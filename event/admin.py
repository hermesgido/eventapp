from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group, Permission
from .models import Event, EventBooking, Venue, VenueBooking
from django import forms

# ... Your model definitions go here ...

# Restrict access to User, Group, and Permission admin based on username
class CustomUserAdmin(UserAdmin):
    def has_module_permission(self, request):
        return request.user.username == "admin"

    def has_view_permission(self, request, obj=None):
        return request.user.username == "admin"

    def has_add_permission(self, request):
        return request.user.username == "admin"

    # def has_change_permission(self, request, obj=None):
    #     return request.user.username == "admin"

    def has_delete_permission(self, request, obj=None):
        return request.user.username == "admin"

class CustomGroupAdmin(GroupAdmin):
    # Repeat the same permission checks for Group
    def has_module_permission(self, request):
        return request.user.username == "admin"

    def has_view_permission(self, request, obj=None):
        return request.user.username == "admin"

    def has_add_permission(self, request):
        return request.user.username == "admin"

    def has_change_permission(self, request, obj=None):
        return request.user.username == "admin"

    def has_delete_permission(self, request, obj=None):
        return request.user.username == "admin"

class CustomPermissionAdmin(admin.ModelAdmin):
    # Repeat the same permission checks for Permission
    def has_module_permission(self, request):
        return request.user.username == "admin"

    def has_view_permission(self, request, obj=None):
        return request.user.username == "admin"

    def has_add_permission(self, request):
        return request.user.username == "admin"

    def has_change_permission(self, request, obj=None):
        return request.user.username == "admin"

    def has_delete_permission(self, request, obj=None):
        return request.user.username == "admin"

# ... Your existing admin classes go here ...

# Register models with the custom admin classes
admin.site.unregister(User)
admin.site.unregister(Group)
# admin.site.unregister(Permission)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)
admin.site.register(Permission, CustomPermissionAdmin)


class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user']  # Exclude the 'user' field

class VenueAdminForm(forms.ModelForm):
    class Meta:
        model = Venue
        exclude = ['user']

class EventBookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'booking_date', 'booking_duration', 'is_approved', 'is_canceled')
    list_filter = ('is_approved', )
    actions = ['approve_selected_bookings']

    def approve_selected_bookings(self, request, queryset):
        # Custom action to approve selected bookings
        queryset.update(is_approved=True)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser and not request.user.username=="admin":
            return qs.filter(event__user=request.user)
        return qs

class VenueBookingAdmin(admin.ModelAdmin):
    list_display = ('venue', 'user', 'booking_date', 'booking_duration', 'is_approved', 'is_canceled')
    list_filter = ('is_approved', )
    actions = ['approve_selected_bookings']

    def approve_selected_bookings(self, request, queryset):
        # Custom action to approve selected bookings
        queryset.update(is_approved=True)

    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser and not request.user.username=="admin":
            return qs.filter(venue__user=request.user)
        return qs.filter(venue__user=request.user)

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity', 'price_per_hour', 'available']
    list_filter = ['location', 'available']
    search_fields = ['name', 'location']
    list_editable = ['available']
    list_per_page = 20
    form = VenueAdminForm


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser and not request.user.username=="admin":
            return qs.filter(user=request.user)
        return qs
    def save_model(self, request, obj, form, change):
        if not change:  # Only set the user field when creating a new venue
            obj.user = request.user
        super().save_model(request, obj, form, change)



from django.utils.html import format_html

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'price', 'time', 'maximum_people', 'display_event_bookings']
    list_filter = ['location', 'maximum_people']
    search_fields = ['name', 'location', 'hosts']
    list_per_page = 20
    form = EventAdminForm 


    def save_model(self, request, obj, form, change):
            if not change:  # Only set the user field when creating a new venue
                obj.user = request.user
            super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser and not request.user.username=="admin":
            return qs.filter(user=request.user)
        return qs

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




