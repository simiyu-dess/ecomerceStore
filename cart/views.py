from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.conf import settings
from Products.models import Product
from django.views.decorators.http import require_POST
from .forms import cartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    form = cartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product, quantity=cd['quantity'], update_quantity=cd['update'])
        
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.remove(product)
     


    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    
    for item in cart:
        item['update_quantity_form'] = cartAddProductForm(initial={'quantity':item['quantity'], 'update':True})
        
    return render(request, "cart.html", {'cart': cart})



# Create your views here.
