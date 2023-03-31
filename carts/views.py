from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from products.models import Product

from .models import Cart
from .models import CartProducts
from .utils import get_or_create_cart

def cart(request):  
  cart = get_or_create_cart(request)

  return render(request, 'carts/cart.html', {
    'cart':cart
  })

def add(request):
  cart = get_or_create_cart(request)
  product = get_object_or_404(Product, pk=request.POST.get('product_id'))
  quantity = request.POST.get('quantity', 1)

  cart.products.add(product, through_defaults={
    'quantity': quantity
  })

  return render(request, 'carts/add.html', {
    'product':product
  })

def remove(request):  
  cart = get_or_create_cart(request)
  product = get_object_or_404(Product, pk=request.POST.get('product_id'))

  cart.products.remove(product)

  return redirect('carts:cart')