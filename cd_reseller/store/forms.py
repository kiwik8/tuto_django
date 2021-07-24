from django import forms
from .models import Variety, Booking

global attrs
attrs = {'class': 'form-control manager'}


class VarietyForm(forms.ModelForm):
    class Meta:
        model = Variety
        fields = ["title", "picture", "price", "stock"]
        widgets = {
            'title': forms.TextInput(attrs=attrs),
            'picture': forms.URLInput(attrs=attrs),
            'price': forms.NumberInput(attrs=attrs),
            'stock': forms.NumberInput(attrs=attrs)
        }


class BookingForm(forms.ModelForm):
    # CAPTCHA HERE
    class Meta:
        model = Booking
        fields = ['quantity', 'address', 'pgp_public_address', 'email']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control manager', 'placeholder': '1/2/3 (grams)'}),
            'address': forms.TextInput(attrs={'class': 'form-control manager', 'placeholder': '25 rue de la Paix 75001 Paris France'}),
            'pgp_address': forms.TextInput(attrs={'class': 'form-control manager pgp'}),
            'email': forms.EmailInput(attrs=attrs),
        }
