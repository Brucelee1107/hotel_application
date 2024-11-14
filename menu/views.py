from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from orders.models import CartItem, Order
from django.contrib.auth.decorators import login_required

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    CartItem.objects.create(user=request.user, menu_item=item, quantity=1)
    return redirect('orders:checkout')

