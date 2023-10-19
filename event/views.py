from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


def home(request):
    venues = [i for i in range (6)]
    events = [i for i in range (6)]
    context = {
        'venues': venues,
        'events': events
    }
    return render(request, 'index.html', context)

def event(request):
    venues = [i for i in range (3)]
    events = [i for i in range (3)]
    context = {
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
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
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
        return redirect('home')  

    return render(request, 'register.html')
