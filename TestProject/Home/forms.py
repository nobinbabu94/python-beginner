from django import forms  # Import forms module
from .models import bookings

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = bookings
        fields = '__all__'
        
        widgets = {
            'booking_date' : DateInput()
        }