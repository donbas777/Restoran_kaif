from django import forms
from .models import Reservation
from django.utils import timezone
import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'special_request']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ім\'я'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш телефон'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '12'}),
            'special_request': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Особливі побажання', 'rows': 3}),
        }
        labels = {
            'name': 'Ім\'я',
            'email': 'Email',
            'phone': 'Телефон',
            'date': 'Дата',
            'time': 'Час',
            'guests': 'Кількість гостей',
            'special_request': 'Особливі побажання',
        }
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        today = timezone.now().date()
        
        if date < today:
            raise forms.ValidationError("Ви не можете забронювати столик на минулу дату.")
        
        # Limit reservations to 3 months in advance
        max_date = today + datetime.timedelta(days=90)
        if date > max_date:
            raise forms.ValidationError("Ви не можете забронювати столик більше ніж на 3 місяці вперед.")
        
        return date
    
    def clean_time(self):
        time = self.cleaned_data.get('time')
        date = self.cleaned_data.get('date')
        
        # Check if the restaurant is open at this time
        opening_time = datetime.time(11, 0)  # 11:00 AM
        closing_time = datetime.time(22, 0)  # 10:00 PM
        
        # Special hours for weekends
        if date and date.weekday() >= 5:  # 5 is Saturday, 6 is Sunday
            if date.weekday() == 6:  # Sunday
                opening_time = datetime.time(12, 0)  # 12:00 PM
            closing_time = datetime.time(23, 0)  # 11:00 PM
        
        if time < opening_time or time > closing_time:
            raise forms.ValidationError(f"Ресторан працює з {opening_time.strftime('%H:%M')} до {closing_time.strftime('%H:%M')}.")
        
        # If reservation is for today, check if the time has already passed
        today = timezone.now().date()
        if date == today and time < timezone.now().time():
            raise forms.ValidationError("Ви не можете забронювати столик на час, що вже минув.")
        
        return time
    
    def clean_guests(self):
        guests = self.cleaned_data.get('guests')
        
        if guests < 1:
            raise forms.ValidationError("Кількість гостей має бути не менше 1.")
        
        if guests > 12:
            raise forms.ValidationError("Для бронювання столика на більше ніж 12 осіб, будь ласка, зателефонуйте нам.")
        
        return guests
