from django.forms import ModelForm, TextInput, EmailInput, URLInput, NumberInput
from .models import Contact, Variety

global attrs
attrs = {'class': 'form-control'}

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email"]
        widgets = {
            'name': TextInput(attrs=attrs),
            'email': EmailInput(attrs=attrs)
        }


class VarietyForm(ModelForm):
    class Meta:
        model = Variety
        fields = ["title", "picture", "price", "stock"]
        widgets = {
            'title': TextInput(attrs=attrs),
            'picture': URLInput(attrs=attrs),
            'price': NumberInput(attrs=attrs),
            'stock': NumberInput(attrs=attrs)
        }
