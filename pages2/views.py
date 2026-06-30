from django.shortcuts import render

def index(request):
    return render(request, 'pages2/index.html')
def about(request):
    return render(request, 'pages2/about.html')
def contact(request):
    return render(request, 'pages2/contact.html')
