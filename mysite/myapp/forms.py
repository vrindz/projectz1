from django import forms
from .models import Booking

class careerform(forms.Form):

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    Apply_For = forms.CharField(max_length=100)
    Attach_Your_Resume = forms.ImageField()
class DateInput(forms.DateInput):
    input_type = 'date'
class BookingForm(forms.ModelForm) :
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'booking_date': DateInput(),
        }
        labels = {
            'p_name': "Patient Name :",
            'p_phone': "Patient Contact number :",
            'p_email': "Patient Email:",
            'doc_name': "Doctor name:",
            'booking_date': "Booking Date:",
        }