from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

from.models import Filtter
# Create your views here.
def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)

def contact(request):
    context = {"is_contact": True}
    return render(request, "web/contact.html", context)

def filtter(request):
    context = {"is_filtter": True}
    filtter = Filtter.objects.all()

    for item in filtter:
        if item.price < 50:
            item.price_class = 'price-low'
        elif item.price >= 50 and item.price < 100:
            item.price_class = 'price-medium'
        else:
            item.price_class = 'price-high'

    context = {"filtter": filtter}
    return render(request, "web/filtter.html", context)



def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:signin')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:signin')
            else:
                customer = User.objects.create_user(username=username,password=pass1)
                return redirect('web:signin')
           

    return render(request,"web/signup.html")
          
def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:index')
    return render(request,"web/signin.html")

def logout_1(request):
    logout(request)
    return redirect('web:index')