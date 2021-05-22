from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, NewImageForm, ImageCommentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .emails import send_welcome_email
from .models import Image, Comment, Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
# def index(request):
#     return render(request, 'registration/login.html', {})

def homepage(request):
    images=Image.objects.all()
    return render(request, 'instaclone/index.html', {"images": images})

def registerUser(request):
    form=RegistrationForm()
    if request.method == "POST":
        form=RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

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

                return redirect('homepage')

            else:
                messages.error(request, "Username or Password is incorrect")

        else:
            messages.error(request, "Field is empty. Enter Username and Password")

    title="Instaclone.com"
    return render(request, 'registration/login.html', {"title":title})


def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required
def new_image(request):
    current_user = request.user
    if request.method=="POST":
        form=NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.profile=current_user
            image.save()

        return redirect('homepage')

    else:
        form=NewImageForm()
    return render(request, 'instaclone/new_image.html', {"form":form})

@login_required
def new_comment(request):
    form=ImageCommentForm()
    all_comments=Comment.objects.all()
    if request.method == "POST":
        form=ImageCommentForm(request.POST)

        if form.is_valid():
            comment=form.cleaned_data['comment']
            comment=ImageCommentForm(comment=comment)
            comment.save()

            return redirect('homepage')

    else:
        form=ImageCommentForm()
 
    return render(request, 'instaclone/oneimage.html', {"form":form, "all_comments":all_comments})