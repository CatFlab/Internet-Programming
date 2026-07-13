from django.shortcuts import redirect, render, get_object_or_404
from .models import Map, Event
from .forms import EventForm


def index(request):
    return render(request, 'index.html', {"active_page": "home"})

def about(request):
    return render(request, 'About_us.html', {"active_page": "about"})

def contact(request):
    return render(request, 'Contact_us.html', {"active_page": "contact"})

def register(request):
    return render(request, 'Register.html', {"active_page": "register"})

def login(request):
    return render(request, 'Login.html', {"active_page": "login"})

def activitycenter(request):
    return render(request, 'Activity_Center.html', {"active_page": "activitycenter"})

def interactivemap(request):
    maps = Map.objects.all()
    return render(request, 'Interactive_Map.html', {"active_page": "map", "maps": maps})


######################### Event Section #########################

def event(request):
    event_form = EventForm()
    events = Event.objects.all()
    return render(request, 'Event/Event.html', {"active_page": "event", "events": events, "event_form": event_form})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'Event/Event_Detail.html', {"active_page": "event", "event": event})

def event_create(request):
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            action = request.POST.get('action')
            if action == 'save_add':
                return redirect('event_create')
            return redirect('event')

        events = Event.objects.all()
        return render(request, 'Event.html', {"active_page": "event", "events": events, "event_form": event_form})

    return redirect('event')

#################################################################