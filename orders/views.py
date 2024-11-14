from django.shortcuts import render, redirect
from .models import CartItem, Order
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    return render(request, 'orders/checkout.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    order = Order.objects.create(user=request.user, total_price=total_price)
    order.items.set(cart_items)
    cart_items.delete()
    return redirect('orders:order_summary', order_id=order.id)

@login_required
def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/checkout.html', {'order': order})

