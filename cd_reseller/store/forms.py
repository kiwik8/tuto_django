from django import forms
from .models import Contact, Variety
from django.utils.safestring import mark_safe

global attrs
attrs = {'class': 'form-control manager'}

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email"]
        widgets = {
            'name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs)
        }


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
