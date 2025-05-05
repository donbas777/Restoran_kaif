from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ім\'я'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема повідомлення'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваше повідомлення', 'rows': 5}),
        }
        labels = {
            'name': 'Ім\'я',
            'email': 'Email',
            'subject': 'Тема',
            'message': 'Повідомлення',
        }
