from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import RegistrationForm, NewImageForm, ImageCommentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .emails import send_welcome_email
from .models import Image, Comment, Profile, User
from django.contrib.auth.decorators import login_required
# Create your views here.
# def index(request):
#     return render(request, 'registration/login.html', {})

def homepage(request):
    images=Image.objects.all()
    users=User.objects.all()
    print(users)
    
    return render(request, 'instaclone/index.html', {"images":images, "users":users})

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

def likes(request, pk):
    imagelike=get_object_or_404(Image, id=request.POST.get('likebutton'))
    imagelike.likes.add(request.user)
    return redirect('homepage')


@login_required
def viewPhoto(request, pk):
    image=Image.objects.get(id=pk)  
    form=ImageCommentForm()
    
    all_comments=Comment.objects.filter(id=pk).all()

    likesonimage=get_object_or_404(Image, id=pk)
    total_likes=likesonimage.total_likes()
   
    if request.method == "POST":
        form=ImageCommentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('homepage')

    else:
        form=ImageCommentForm()
    return render(request, 'instaclone/oneimage.html', {"image": image, "form":form, "all_comments": all_comments,"total_likes": total_likes})

@login_required
def profile_view(request, pk):
    user=Profile.objects.filter(id=pk)

    return render(request, "instaclone/profile.html", {"user":user})

