from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('category/<slug:category_slug>/', views.menu_by_category, name='menu_by_category'),
    path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),
]
