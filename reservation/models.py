from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"

class Reservation(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    special_request = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date', '-time']
    
    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"
    
    @property
    def is_past(self):
        reservation_datetime = timezone.make_aware(
            timezone.datetime.combine(self.date, self.time)
        )
        return reservation_datetime < timezone.now()
