from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'About_us.html')

def contact(request):
    return render(request, 'Contact_us.html')

def event(request):
    return render(request, 'Event.html')

def register(request):
    return render(request, 'Register.html')

def login(request):
    return render(request, 'Login.html')

def activitycenter(request):
    return render(request, 'Activity_Center.html')

def interactivemap (request):
    return render(request, 'Interactive_Map.html')