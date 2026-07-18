from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from .models import Map, Event
from .forms import EventForm 
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html', {"active_page": "home"})

def about(request):
    return render(request, 'About_us.html', {"active_page": "about"})

def contact(request):
    return render(request, 'Contact_us.html', {"active_page": "contact"})

def activitycenter(request):
    return render(request, 'Activity_Center.html', {"active_page": "activitycenter"})

def interactivemap(request):
    maps = Map.objects.all()
    return render(request, 'Interactive_Map.html', {"active_page": "map", "maps": maps})

######################### Register Section #########################

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/Register.html', {'form': form})



######################### Event Section #########################

def event(request):
    event_form = EventForm()
    if request.user.is_authenticated:
        events = Event.objects.filter(user=request.user)
    else:
        events = Event.objects.filter(user__is_superuser=True)
    return render(request, 'Event/Event.html', {"active_page": "event", "events": events, "event_form": event_form})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'Event/Event_Detail.html', {"active_page": "event", "event": event})

@login_required
def event_create(request):
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.user = request.user
            event.save()
            action = request.POST.get('action')
            if action == 'save_add':
                return redirect('event_create')
            return redirect('event')

        events = Event.objects.all()
        return render(request, 'event/Event.html', {"active_page": "event", "events": events, "event_form": event_form})

    return redirect('event')

@login_required
def event_edit(request, id):
    event = get_object_or_404(Event, id=id, user=request.user)
    if request.method == "POST":
        event_form = EventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
            return redirect('event_detail', id=event.id)

    event_form = EventForm(instance=event)
    return render(request, 'Event/Event_Edit.html', {"active_page": "event", "event": event, "event_form": event_form})

@login_required
def event_delete(request, id):
    event = get_object_or_404(Event, id=id, user=request.user)
    if request.method == "POST":
        event.delete()
        return redirect('event')
    return render(request, 'Event/Event_Delete.html', {"active_page": "event", "event": event})
    
#################################################################