from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('About_us.html', views.about, name='about'),
    path('Contact_us.html', views.contact, name='contact'),
    
######################### Event Section #########################

    path('Event.html', views.event, name='event'),
    path('event-create/', views.event_create, name='event_create'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),
    path('event/<int:id>/edit/', views.event_edit, name='event_edit'),
    path('event/<int:id>/delete/', views.event_delete, name='event_delete'),

#################################################################

    path('registration/Register.html', views.register, name='register'),
    path('registration/Login.html', auth_views.LoginView.as_view(), name='login'),
    path('registration/Logout.html', auth_views.LogoutView.as_view(), name='logout'),
    path('Activity_Center.html', views.activitycenter, name='activitycenter'),
    path('Interactive_map.html', views.interactivemap, name='interactivemap'),
]