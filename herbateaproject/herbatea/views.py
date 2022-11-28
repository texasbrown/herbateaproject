from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'herbatea/home.html ', {})

def signin(request):
    return render(request, 'herbatea/signin.html', {} )

def signup(request):
    return render(request, 'herbatea/signup.html', {})

def trackorder(request):
    return render(request, 'herbatea/trackorder.html', {})