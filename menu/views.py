from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Category, Dish
from order.models import Cart, CartItem

# Create your views here.

def menu_list(request):
    # Get all categories
    categories = Category.objects.all()
    
    # Get all available dishes
    dishes = Dish.objects.filter(is_available=True)
    
    context = {
        'categories': categories,
        'dishes': dishes,
    }
    
    return render(request, 'menu/menu_list.html', context)

def menu_by_category(request, category_slug):
    # Get the category
    category = get_object_or_404(Category, slug=category_slug)
    
    # Get all available dishes in this category
    dishes = Dish.objects.filter(category=category, is_available=True)
    
    context = {
        'category': category,
        'dishes': dishes,
    }
    
    return render(request, 'menu/menu_by_category.html', context)

def dish_detail(request, dish_id):
    # Get the dish
    dish = get_object_or_404(Dish, id=dish_id, is_available=True)
    
    # Get related dishes (same category)
    related_dishes = Dish.objects.filter(category=dish.category, is_available=True).exclude(id=dish.id)[:4]
    
    context = {
        'dish': dish,
        'related_dishes': related_dishes,
    }
    
    return render(request, 'menu/dish_detail.html', context)
