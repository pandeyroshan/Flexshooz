from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from users.models import cart,wishList
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'store/index.html',{'products': products})

# add to cart
@login_required
def add_to_cart(request,p_id):
    product_object = Product.objects.get(id=p_id)
    cart_object = cart.objects.get(user=request.user)
    cart_object.productID.add(product_object)
    cart_object.save()
    return redirect('/')


# add to wishlist
@login_required
def add_to_wishlist(request,p_id):
    product_object = Product.objects.get(id=p_id)
    wishlist_object = wishList.objects.get(user=request.user)
    wishlist_object.productID.add(product_object)
    wishlist_object.save()
    return redirect('/')


# remove from cart
@login_required
def remove_from_cart(request,p_id):
    product_object = Product.objects.get(id=p_id)
    cart_object = cart.objects.get(user=request.user)
    cart_object.productID.remove(product_object)
    cart_object.save()
    return redirect('/')


# remove from wishlist
@login_required
def remove_from_wishlist(request,p_id):
    product_object = Product.objects.get(id=p_id)
    wishlist_object = wishList.objects.get(user=request.user)
    wishlist_object.productID.remove(product_object)
    wishlist_object.save()
    return redirect('/')
