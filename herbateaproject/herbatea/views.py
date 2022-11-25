from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'herbatea/home.html ', {})

def index(request):
    return render(request, 'herbatea/index.html', {} )

def signup(request):
    return render(request, 'herbatea/signup.html', {})