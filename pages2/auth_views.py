from django.shortcuts import render

def login(request):
    return render(request, 'registration/Login.html', {"active_page": "login"})