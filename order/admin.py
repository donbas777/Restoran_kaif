from django.contrib import admin
from .models import Order, OrderItem, Cart, CartItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['dish']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'delivery_method', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'delivery_method', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [OrderItemInline]
    list_editable = ('status',)

class CartItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['dish']
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_id', 'created_at', 'get_total_items', 'get_total_price')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'session_id')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CartItemInline]
