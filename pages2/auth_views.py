from django.shortcuts import render

def login(request):
    return render(request, 'registration/Login.html', {"page_active": "login"})