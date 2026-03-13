from django.shortcuts import redirect,render
from .models import Cart
from products.models import Product


def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    Cart.objects.create(
        user=request.user,
        product=product,
        quantity=1
    )

    return redirect('cart')



def cart_view(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    context = {
        'cart_items': cart_items,
        'total': total
    }

    return render(request, 'cart/cart.html', context)

#Increase Quantity View

def increase_quantity(request, cart_id):

    cart = Cart.objects.get(id=cart_id)

    cart.quantity += 1

    cart.save()

    return redirect('cart')

#Decrease Quantity View

def decrease_quantity(request, cart_id):

    cart = Cart.objects.get(id=cart_id)

    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()

    return redirect('cart')

#Remove Item from Cart

def remove_item(request, cart_id):

    cart = Cart.objects.get(id=cart_id)

    cart.delete()

    return redirect('cart')
