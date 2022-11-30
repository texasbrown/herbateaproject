from django.shortcuts import render, redirect
from .models import *
from .forms import CustomerForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'store/register.html', context)

def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request, 'store/login.html', context)




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


#def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        Customer = authenticate(request, email=email, password=password)

        if Customer is not None:
            login(request, Customer)
            return redirect('home')
        else:
            messages.success(request, ("Error Logging in"))
            return redirect('login')

    context = {}
    return render(request, 'store/login.html', context)

#def login(request):
#    context = {}
 #   return render(request, 'store/login.html', context)

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