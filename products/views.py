from django.shortcuts import render
from .models import Product

def home(request):
    return render(request,'home.html')

def product_list(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/product_list.html', context)

def product_detail(request, id):

    product = Product.objects.get(id=id)

    return render(request,'products/product_detail.html',{'product':product})