from django.shortcuts import render, redirect
from .models import *
from .decorators import unauthenticated_user, allowed_users
import json
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import Group


@unauthenticated_user
def registerPage(request):
   
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='customer')
                user.groups.add(group)

                Customer.objects.create(
                    user=user,
                    )
                messages.success(request, 'Account was created for ' + username)
                return redirect('login')

        context = {'form':form}
        return render(request, 'store/register.html', context)


@unauthenticated_user
def loginPage(request):
  
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('products')
            else:
                messages.info(request, 'Username OR password incorrect')

        context = {}
        return render(request, 'store/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



##@allowed_users(allowed_roles=['admin', 'customer'])
def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/home.html', context)

def signup(request):
    if request.method == "POST":
         form = CustomerForm(request.POST or None)
         if form.is_valid():
            form.save()
            messages.success(request, ('Submitted Successfully'))
         return redirect('products')
    else:
         return render(request, 'store/signup.html', {})


def about(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/about.html', {'title': 'About'})

def products(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'store/products.html', context)

@login_required(login_url='login')
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

@login_required(login_url='login')
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def contact(request):
    if request.method == "POST":
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Submitted Successfully'))
        return redirect('thankyou')
    else:
        return render(request, 'store/contact.html')
    

def thankyou(request):
    context = {}
    return render(request, 'store/thankyou.html', context)

@login_required(login_url='login')
def placedorder(request):
    orders = Order.objects.all()
    context = {'order_history':orders}
    return render(request, 'store/placedorder.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action', action)
    print('productId', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
