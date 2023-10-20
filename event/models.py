from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    maximum_people = models.IntegerField()
    hosts = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='event_photos/', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='venue_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class EventBooking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_duration = models.PositiveIntegerField()
    is_approved = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return self.event.name


    # Add any other fields specific to event bookings

class VenueBooking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_duration = models.PositiveIntegerField()
    is_approved = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return self.venue.name

    # Add any other fields specific to venue bookings
