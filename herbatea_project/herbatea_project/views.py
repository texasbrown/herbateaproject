from django.shortcuts import render

def home(request):
    return render(request, 'herbatea_project/home.html')

def login(request):
    return render(request, 'herbatea_project/login.html')

def signup(request):
    return render(request, 'herbatea_project/signup.html')