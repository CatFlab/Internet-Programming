from django.shortcuts import render
from .models import Map, Event


def index(request):
    return render(request, 'index.html', {"active_page": "home"})

def about(request):
    return render(request, 'About_us.html', {"active_page": "about"})

def contact(request):
    return render(request, 'Contact_us.html', {"active_page": "contact"})

def event(request):
    events = Event.objects.all()
    return render(request, 'Event.html', {"active_page": "event", "events": events})

def register(request):
    return render(request, 'Register.html', {"active_page": "register"})

def login(request):
    return render(request, 'Login.html', {"active_page": "login"})

def activitycenter(request):
    return render(request, 'Activity_Center.html', {"active_page": "activitycenter"})

def interactivemap(request):
    maps = Map.objects.all()
    return render(request, 'Interactive_Map.html', {"active_page": "map", "maps": maps})