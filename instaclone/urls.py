from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="loginuser"),
    path('register/', views.registerUser, name="registeruser"),
    path('logout/', views.logoutUser, name="logout")
]