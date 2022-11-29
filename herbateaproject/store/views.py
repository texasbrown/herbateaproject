from django.shortcuts import render
from .models import Orders

# Create your views here.
def home(request):
    return render(request, 'herbatea/home.html ', {})

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