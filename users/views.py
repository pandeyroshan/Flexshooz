from django.shortcuts import render,redirect
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    if request.method=='POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            return redirect(request.META.get('HTTP_REFERER'))
    return render(request,'users/login.html')