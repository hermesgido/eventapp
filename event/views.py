from django.shortcuts import render

# Create your views here.


def home(request):
    venues = [i for i in range (6)]
    events = [i for i in range (6)]
    context = {
        'venues': venues,
        'events': events
    }
    return render(request, 'index.html', context)
