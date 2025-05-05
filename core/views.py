from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import TeamMember, Testimonial
from .forms import ContactForm
from menu.models import Dish, Category
from events.models import Event, Promotion

# Create your views here.

def home(request):
    # Get featured dishes (special dishes)
    featured_dishes = Dish.objects.filter(is_special=True, is_available=True)[:6]
    
    # Get active testimonials
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    
    # Get upcoming events (filter by date instead of is_past property)
    today = timezone.now().date()
    upcoming_events = Event.objects.filter(start_date__gte=today)[:3]
    
    # Get active promotions
    active_promotions = Promotion.objects.filter(
        is_active=True, 
        start_date__lte=today,
        end_date__gte=today
    )[:2]
    
    context = {
        'featured_dishes': featured_dishes,
        'testimonials': testimonials,
        'upcoming_events': upcoming_events,
        'active_promotions': active_promotions,
        'today': today,
    }
    
    return render(request, 'core/home.html', context)

def about(request):
    # Get team members
    team_members = TeamMember.objects.all()
    
    # Get all testimonials
    testimonials = Testimonial.objects.filter(is_active=True)
    
    context = {
        'team_members': team_members,
        'testimonials': testimonials,
    }
    
    return render(request, 'core/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше повідомлення успішно надіслано! Ми зв\'яжемося з вами найближчим часом.')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'core/contact.html', context)
