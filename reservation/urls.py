from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.reservation_form, name='reservation_form'),
    path('confirm/', views.reservation_confirm, name='reservation_confirm'),
    path('success/', views.reservation_success, name='reservation_success'),
]
