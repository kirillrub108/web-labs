from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from products.models import Product,Pozition_Price
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)# инициализация корзины

    product=Pozition_Price.objects.get(id=product_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                  update_quantity=cd['update'])
    return redirect(reverse('cart_detail'))

def cart_remove(request, product_id):
    cart = Cart(request)
    product=Pozition_Price.objects.get(id=product_id)
    cart.remove(product)
    return redirect(reverse('cart_detail'))

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
