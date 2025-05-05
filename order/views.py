from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Cart, CartItem, Order, OrderItem
from .forms import OrderForm
from menu.models import Dish

def _get_or_create_cart(request):
    """Helper function to get or create a cart for the current session."""
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key
    
    cart, created = Cart.objects.get_or_create(session_id=session_id)
    return cart

def cart(request):
    cart = _get_or_create_cart(request)
    cart_items = cart.items.all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    
    return render(request, 'order/cart.html', context)

def add_to_cart(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id, is_available=True)
    cart = _get_or_create_cart(request)
    
    # Get quantity from form, default to 1
    quantity = int(request.POST.get('quantity', 1))
    
    # Check if the dish is already in the cart
    try:
        cart_item = CartItem.objects.get(cart=cart, dish=dish)
        # Update quantity
        cart_item.quantity += quantity
        cart_item.save()
        messages.success(request, f'Кількість "{dish.name}" оновлено у кошику.')
    except CartItem.DoesNotExist:
        # Create new cart item
        CartItem.objects.create(cart=cart, dish=dish, quantity=quantity)
        messages.success(request, f'"{dish.name}" додано до кошика.')
    
    # Redirect back to the referring page
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('menu:menu_list')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    messages.success(request, 'Товар видалено з кошика.')
    
    return redirect('order:cart')

def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    try:
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Кількість оновлено.')
        else:
            cart_item.delete()
            messages.success(request, 'Товар видалено з кошика.')
    except:
        messages.error(request, 'Неправильна кількість.')
    
    return redirect('order:cart')

def checkout(request):
    cart = _get_or_create_cart(request)
    cart_items = cart.items.all()
    
    if not cart_items:
        messages.warning(request, 'Ваш кошик порожній. Додайте товари перед оформленням замовлення.')
        return redirect('menu:menu_list')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            
            # Set total price
            order.total_price = cart.get_total_price()
            order.save()
            
            # Create order items from cart items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    dish=cart_item.dish,
                    quantity=cart_item.quantity,
                    price=cart_item.dish.price
                )
            
            # Clear the cart
            cart_items.delete()
            
            # Store order ID in session for success page
            request.session['order_id'] = order.id
            
            messages.success(request, 'Ваше замовлення успішно оформлено!')
            return redirect('order:order_success')
    else:
        form = OrderForm()
    
    context = {
        'form': form,
        'cart': cart,
        'cart_items': cart_items,
    }
    
    return render(request, 'order/checkout.html', context)

def order_success(request):
    order_id = request.session.get('order_id')
    
    if not order_id:
        return redirect('menu:menu_list')
    
    order = get_object_or_404(Order, id=order_id)
    
    # Clear the session
    if 'order_id' in request.session:
        del request.session['order_id']
    
    context = {
        'order': order,
    }
    
    return render(request, 'order/order_success.html', context)
