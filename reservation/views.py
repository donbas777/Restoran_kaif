from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Reservation, Table
from .forms import ReservationForm

# Create your views here.

def reservation_form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Save the reservation but don't commit to DB yet
            reservation = form.save(commit=False)
            
            # Check if there are available tables for the requested date, time, and guests
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            guests = form.cleaned_data['guests']
            
            # Find tables that can accommodate the guests
            suitable_tables = Table.objects.filter(capacity__gte=guests, is_available=True)
            
            # Check if any of these tables are already reserved for the same date and time
            reserved_tables = Reservation.objects.filter(
                date=date,
                time=time,
                status='confirmed'
            ).values_list('table', flat=True)
            
            # Filter out already reserved tables
            available_tables = suitable_tables.exclude(id__in=reserved_tables)
            
            if available_tables.exists():
                # Assign the first available table
                reservation.table = available_tables.first()
                reservation.save()
                
                # Store reservation ID in session for confirmation
                request.session['reservation_id'] = reservation.id
                
                return redirect('reservation:reservation_confirm')
            else:
                messages.error(request, 'На жаль, немає вільних столиків на вказаний час. Будь ласка, виберіть інший час або дату.')
    else:
        form = ReservationForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'reservation/reservation_form.html', context)

def reservation_confirm(request):
    # Get reservation from session
    reservation_id = request.session.get('reservation_id')
    
    if not reservation_id:
        return redirect('reservation:reservation_form')
    
    reservation = Reservation.objects.get(id=reservation_id)
    
    if request.method == 'POST':
        # Confirm the reservation
        reservation.status = 'confirmed'
        reservation.save()
        
        # Clear the session
        if 'reservation_id' in request.session:
            del request.session['reservation_id']
        
        messages.success(request, 'Ваше бронювання успішно підтверджено!')
        return redirect('reservation:reservation_success')
    
    context = {
        'reservation': reservation,
    }
    
    return render(request, 'reservation/reservation_confirm.html', context)

def reservation_success(request):
    return render(request, 'reservation/reservation_success.html')
