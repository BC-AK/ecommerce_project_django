from django.shortcuts import render, redirect
from cart.models import Cart
from .models import Order

#Create Checkout View
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
def place_order(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    order = Order.objects.create(
        user=request.user,
        total_price=total
    )

    cart_items.delete()

    return redirect('order_success')

#Order Success Page
def order_success(request):

    return render(request,'orders/success.html')