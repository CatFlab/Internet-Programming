from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('About_us.html', views.about, name='about'),
    path('Contact_us.html', views.contact, name='contact'),
    
######################### Event Section #########################

    path('Event.html', views.event, name='event'),
    path('event-create/', views.event_create, name='event_create'),
    path('event/<int:id>/', views.event_detail, name='detail_event'),

#################################################################

    path('Register.html', views.register, name='register'),
    path('Login.html', views.login, name='login'),
    path('Activity_Center.html', views.activitycenter, name='activitycenter'),
    path('Interactive_map.html', views.interactivemap, name='interactivemap'),
]