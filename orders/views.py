from django.shortcuts import render, redirect
from cart.models import Cart
from .models import Order
from django.contrib.auth.decorators import login_required

#Create Checkout View
@login_required
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    context = {
        'cart_items': cart_items,
        'total': total
    }

    return render(request, 'orders/checkout.html', context)

#Create Place Order View
@login_required
def place_order(request):

    cart_items = Cart.objects.filter(user=request.user)

    for item in cart_items:
        Order.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return redirect('order_success')

#Order History View
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})

#Order Success Page
@login_required
def order_success(request):

    return render(request,'orders/success.html')