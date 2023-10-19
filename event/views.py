from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from . models import *


# Create your views here.


def home(request):
   

    venues = [i for i in range (6)]
    events = Event.objects.all()
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

def venue(request):
    venues = [i for i in range (3)]
    events = [i for i in range (3)]
    context = {
        'venues': venues,
        'events': events
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


def book_event(request):
    if not request.user.is_authenticated:
        print(request.POST.get('event_id'))
        messages.info(request, "Please Login to proceed")
        return redirect(login_view)
    if request.method == "POST":
        user = request.user
        event_id = request.POST.get('event_id')
        event = Event.objects.get(id=event_id)
        booking_duration = 0
        max_people = event.maximum_people
        if EventBooking.objects.filter(event=event).count() > max_people:
            messages.error(request, "Event is full")
            return redirect('home')
        if EventBooking.objects.filter(event=event, user=user).exists():
            messages.error(request, "You have already booked this event")
            return redirect('home')
            
        EventBooking.objects.create(user=user, event=event, booking_duration=booking_duration)
        messages.success(request, "Event booked successfully")
        return redirect('home')
    else:
        messages.error(request, "Something went wrong")
        return redirect('home')
    

