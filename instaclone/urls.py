from django.urls import path
from . import views

urlpatterns=[
    path('', views.loginUser, name="index"),
    path('homepage/', views.homepage, name="homepage"),   
    path('register/', views.registerUser, name="registeruser"),
    path('uploadimage/', views.new_image, name="uploadimage"),
    path('logout/', views.logoutUser, name="logout")
]