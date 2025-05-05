from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event, Promotion

# Create your views here.

def event_list(request):
    # Get all upcoming events (filter by date instead of is_past property)
    today = timezone.now().date()
    upcoming_events = Event.objects.filter(start_date__gte=today)
    
    # Get all active promotions
    active_promotions = Promotion.objects.filter(
        is_active=True,
        start_date__lte=today,
        end_date__gte=today
    )
    
    context = {
        'upcoming_events': upcoming_events,
        'active_promotions': active_promotions,
        'today': today,
    }
    
    return render(request, 'events/event_list.html', context)

def event_detail(request, event_id):
    # Get the event
    event = get_object_or_404(Event, id=event_id)
    
    # Get related events (upcoming events)
    today = timezone.now().date()
    related_events = Event.objects.filter(start_date__gte=today).exclude(id=event.id)[:3]
    
    context = {
        'event': event,
        'related_events': related_events,
        'today': today,
    }
    
    return render(request, 'events/event_detail.html', context)
