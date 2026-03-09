from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'email': 'Email',
            'address': 'Adresse',
            'postal_code': 'Code postal',
            'city': 'Ville',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'votre@email.com'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 rue de la Paix'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '75001'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Paris'}),
        }
