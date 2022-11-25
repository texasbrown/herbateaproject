from django.shortcuts import render


def index(request):
    return render(request, 'herbatea/index.html')

def signup(request):
    return render(request, 'herbatea/signup.html')
