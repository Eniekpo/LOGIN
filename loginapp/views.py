from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

import loginapp

# Create your views here.


def home(request):
    return render(request, 'loginapp/home.html')
# Create your views here.


def signup(request):
    if request.method == 'POST':
        # firstname = request.POST.get('firstname')
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Registration Successful")
        return redirect('signin')

    return render(request, 'loginapp/signup.html')
# Create your views here.


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'loginapp/home.html', {'fname': fname})
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')



    return render(request, 'loginapp/signin.html')
# Create your views here.


def signout(request):
    pass
