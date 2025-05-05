from django.contrib import admin
from .models import Event, Promotion

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_free', 'is_past', 'is_ongoing')
    list_filter = ('start_date', 'end_date', 'is_free')
    search_fields = ('title', 'description', 'location')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_free',)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'discount_percent', 'discount_amount', 'is_active', 'is_valid')
    list_filter = ('start_date', 'end_date', 'is_active')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active',)
