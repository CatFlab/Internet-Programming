from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'organizer', 'description', 'date', 'time', 'room']
        widgets = {
            "date": forms.DateInput(attrs={
                "placeholder": "YYYY-MM-DD",
            }),
            "time": forms.TimeInput(attrs={
                "placeholder": "HH:MM:SS",
            }),
        }