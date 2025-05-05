from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'delivery_method']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ім\'я'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше прізвище'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш телефон'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Адреса доставки', 'rows': 3}),
            'delivery_method': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'first_name': 'Ім\'я',
            'last_name': 'Прізвище',
            'email': 'Email',
            'phone': 'Телефон',
            'address': 'Адреса',
            'delivery_method': 'Спосіб отримання',
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Simple phone validation - remove spaces and check if it's a number
        phone = phone.replace(' ', '')
        if not phone.isdigit():
            raise forms.ValidationError("Будь ласка, введіть коректний номер телефону (тільки цифри).")
        return phone
    
    def clean(self):
        cleaned_data = super().clean()
        delivery_method = cleaned_data.get('delivery_method')
        address = cleaned_data.get('address')
        
        if delivery_method == 'delivery' and not address:
            self.add_error('address', "Адреса обов'язкова для доставки.")
        
        return cleaned_data
