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
def remove_from_cart(request,id):
    product_object = Product.objects.get(id=id)
    cart_object = cart.objects.get(user=request.user)
    cart_object.productID.remove(product_object)
    cart_object.save()
    return redirect('/cart')


# remove from wishlist
@login_required
def remove_from_wishlist(request,id):
    product_object = Product.objects.get(id=id)
    wishlist_object = wishList.objects.get(user=request.user)
    wishlist_object.productID.remove(product_object)
    wishlist_object.save()
    return redirect('/')

def get_cart(request):
    cartObject = cart.objects.filter(user=request.user).values("productID")
    myList = []
    try:
        for data in cartObject:
            id = data['productID']
            myList.append(Product.objects.get(id=id))
    except:
        pass
    price = 0
    for data in myList:
        price+=data.price
    return render(request,'store/cart.html',{'items': myList,'price':price})