from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'instaclone/index.html', {})

def registerUser(request):
    form=RegistrationForm()
    if request.method == "POST":
        form=RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('loginuser')

    else:
        form=RegistrationForm()
    title="Register New User"
    return render(request, 'registration/registration.html', {"title":title, "form":form})

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        # print(username)
        password = request.POST.get('password')
        # print(password)

        if username and password:
            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('index')

            else:
                messages.error(request, "Username or Password is incorrect")

        else:
            messages.error(request, "Field is empty. Enter Username and Password")

    title="Login User"
    return render(request, 'registration/login.html', {"title":title})


def logoutUser(request):
    logout(request)
    return redirect('index')

