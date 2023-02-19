from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'loginapp/home.html')
# Create your views here.


def signup(request):
    return render(request, 'loginapp/signup.html')
# Create your views here.


def signin(request):
    return render(request, 'loginapp/signin.html')
# Create your views here.


def signout(request):
    pass
