from io import BytesIO
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from . models import *
import qrcode

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import qrcode
from django.core.files.uploadedfile import SimpleUploadedFile

APIKEY = "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"

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.template.loader import render_to_string

def send_email_send(subject, to_email, context):
    email_content = render_to_string('email_template.html', context)

    message = Mail(
        from_email='jacksonkabanza1@gmail.com',
        to_emails=to_email,
        subject=subject,
        html_content=email_content
    )

    try:
        sg = SendGridAPIClient(APIKEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)



def approve_event_booking(booking_id):
    event_booking = EventBooking.objects.get(pk=booking_id)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"Booking ID: {event_booking.pk}\nEvent Name: {event_booking.event.name}\nCustomer Name: {event_booking.user.username}\nPrice Paid: {event_booking.event.price}")

    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Convert the image to binary data and save it in the booking
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    event_booking.qr_code = SimpleUploadedFile(f"qr_{event_booking.pk}.png", buffer.getvalue())
    event_booking.save()

def approve_venue_booking(booking_id):
    venue_booking = VenueBooking.objects.get(pk=booking_id)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"Booking ID: {venue_booking.id}\nVenue Name: {venue_booking.venue.name}\nCustomer Name: {venue_booking.user.username}\nPrice Paid: {venue_booking.venue.price_per_hour}")

    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Convert the image to binary data and save it in the booking
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    venue_booking.qr_code = SimpleUploadedFile(f"qr_{venue_booking.pk}.png", buffer.getvalue())
    vn = venue_booking.venue
    vn.available=False
    vn.save()
    venue_booking.save()

def cancel_book_event(request):
    if request.method == "POST":
        booking_id = request.POST.get('booking_id')
        book = EventBooking.objects.get(id=booking_id)
        book.is_canceled = True

        book.save()
        messages.success(request, "Booking Canceled Succesfull")
        return redirect(bookings)

def cancel_book_venue(request):
    if request.method == "POST":
        booking_id = request.POST.get('booking_id')
        book = VenueBooking.objects.get(id=booking_id)
        book.is_canceled = True

        vn = book.venue
        vn.available=True
        vn.save()        
        book.save()
        messages.success(request, "Booking Canceled Succesfull")
        return redirect(bookings_venue)



def home(request):
   

    venues = Venue.objects.all()
    events = Event.objects.all()
    # for ev in events:
    #     ev.user=request.user
    #     ev.save()
    # for v in venues:
    #     v.user = request.user
    #     v.save()
    context = {
        'venues': venues,
        'events': events
    }
    return render(request, 'index.html', context)

def event(request, id):
    event = Event.objects.get(id=id)

    venues = [i for i in range (3)]
    events =  Event.objects.all()[:3]
    context = {
        'event':event,
        'venues': venues,
        'events': events
    }
    return render(request, 'event.html', context)

def venue(request, id):
    venue = Venue.objects.get(id=id)
    venues =  Venue.objects.all()[:3]
    context = {
        'venue':venue,
        'venues': venues,
    }
    return render(request, 'venue.html', context)


def login_view(request):
    print("THis page is loaded")
    if request.method == 'POST':
        print("THis page reduest is post")

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        if not email or not phone or not password:
            messages.error(request, 'Please fill all fields')
            return redirect('register')
        
        if len(password) < 4:
            messages.error(request, 'Password must be at least 4 characters')
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'User already exists')
            return redirect('register')
        if User.objects.filter(username=phone).exists():
            messages.error(request, 'User already exists')
            return redirect('register')
    
        user = User.objects.create_user(username=email, password=password)
        login(request, user)
        messages.success(request, "Successfull registered")
        return redirect('home')  

    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    messages.info(request, "You have succesfull logged out")
    return redirect('home')

def bookings(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please Login to proceed")
        return redirect(login_view)
    bookings = EventBooking.objects.filter(user=request.user)
    context = {
        'bookings': bookings
    }

    return render(request, 'bookings.html', context)

def bookings_venue(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please Login to proceed")
        return redirect(login_view)
    bookings = VenueBooking.objects.filter(user=request.user)
    context = {
        'bookings': bookings
    }

    return render(request, 'bookings_venue.html', context)


def book_event(request):
    if not request.user.is_authenticated:
        print(request.POST.get('event_id'))
        messages.info(request, "Please Login to proceed")
        return redirect(login_view)
    if request.method == "POST":
        user = request.user
        event_id = request.POST.get('event_id')
        no_of_seats = int(request.POST.get('no_of_seats', 1))  # Default to 1 seat if none provided

        event = Event.objects.get(id=event_id)
        booking_duration = 0
        max_people = event.maximum_people
        if EventBooking.objects.filter(event=event).count() > max_people:
            messages.error(request, "Event is full")
            return redirect('home')
        # if EventBooking.objects.filter(event=event, user=user).exists():
        #     messages.error(request, "You have already booked this event")
        #     return redirect('home')
        
        for i in range(no_of_seats):
            booking = EventBooking.objects.create(user=user, event=event, booking_duration=booking_duration)
            approve_event_booking(booking.id)
            context = {
            'event': event,  # Pass the event and booking details
            'booking': EventBooking.objects.get(id=booking.id),
             }
            try:
               send_email_send('Event Booking Confirmation', 'mariojaxn1@gmail.com', context)
            except:
                messages.info("Error in sending email")

        messages.success(request, "Event booked successfully")
        return redirect('home')
    else:
        messages.error(request, "Something went wrong")
        return redirect('home')
    


def book_venue(request):
    if not request.user.is_authenticated:
        print(request.POST.get('venue_id'))
        messages.info(request, "Please Login to proceed")
        return redirect(login_view)
    if request.method == "POST":
        user = request.user
        venue_id = request.POST.get('venue_id')
        venue = Venue.objects.get(id=venue_id)
        booking_duration = 0
        max_people = venue.capacity
        # if EventBooking.objects.filter(event=event).count() > max_people:
        #     messages.error(request, "Event is full")
        #     return redirect('home')
        if venue.available == False:
            messages.error(request, "Venue is already booked")
            return redirect('home')
        # if VenueBooking.objects.filter(venue=venue, user=user).exists():
        #     messages.error(request, "You have already booked this venue")
        #     return redirect('home')
        
    
        booking = VenueBooking.objects.create(user=user, venue=venue, booking_duration=booking_duration)
        approve_venue_booking(booking.id)
        context = {
        'event': event,  # Pass the event and booking details
        'booking': VenueBooking.objects.get(id=booking.id),
            }
        try:
            send_email_send('Venue Booking Confirmation', 'mariojaxn1@gmail.com', context)
        except:
            messages.info("Error in sending email")

        messages.success(request, "Venue booked successfully")
        return redirect('home')
    else:
        messages.error(request, "Something went wrong")
        return redirect('home')
    
