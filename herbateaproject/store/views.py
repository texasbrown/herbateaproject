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

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)