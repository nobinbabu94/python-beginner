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

        labels ={
              "patient_name" : "Patient Name",
    "patient_phone" : "Patient Phone",
    "patient_email": "Patient Email",
    "docs_name" :"Doctor Name",
    "booking_date" : "Booking Date",
        }