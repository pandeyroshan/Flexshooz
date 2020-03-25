from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import cart,wishList

# Create your views here.

def register(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('cnf_password'):
            user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
            user.save()
            user_cart = cart.objects.create(user=user)
            user_cart.save()
            user_wishlist = wishList.objects.create(user=user)
            user_wishlist.save()
            return redirect('/login')
        else:
            message = 'Password are not same'
    return render(request,'users/register.html')