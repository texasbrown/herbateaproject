from django.shortcuts import render, redirect
from .models import *
from .forms import CustomerForm
from django.contrib import messages


def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def signup(request):
    if request.method == "POST":
         form = CustomerForm(request.POST or None)
         if form.is_valid():
            form.save()
            messages.success(request, ('Submitted Successfully'))
         return redirect('home')
    else:
         return render(request, 'store/signup.html', {})


def login(request):
    context = {}
    return render(request, 'store/login.html', context)

def about(request):
    return render(request, 'store/about.html', {'title': 'About'})

def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/products.html', context)

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

def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def thankyou(request):
    context = {}
    return render(request, 'store/thankyou.html', context)