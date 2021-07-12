from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={'class' : 'form-control'}),
        required=True
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class' : 'form-control'}),
        required=True
        )
    
