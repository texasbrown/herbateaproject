from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'herbatea/home.html ', {})

def about(request):
    return render(request, 'store/about.html', {'title': 'About'})

def signin(request):
    return render(request, 'herbatea/signin.html', {} )

def signup(request):
    return render(request, 'herbatea/signup.html', {})

def trackorder(request):
    return render(request, 'herbatea/trackorder.html', {})

def orders(request):
    orders_list = Orders.objects.all()
    return render(request, 'herbatea/orders.html', 
    { 'orders': orders_list })

def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def thankyou(request):
    context = {}
    return render(request, 'store/thankyou.html', context)