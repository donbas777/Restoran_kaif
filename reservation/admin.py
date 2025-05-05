from django.contrib import admin
from .models import Table, Reservation

# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity', 'is_available')
    list_filter = ('capacity', 'is_available')
    search_fields = ('number',)
    list_editable = ('is_available',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'guests', 'status', 'created_at')
    list_filter = ('date', 'time', 'status', 'created_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at',)
    list_editable = ('status',)
