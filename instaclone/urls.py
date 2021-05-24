from django.urls import path
from . import views

urlpatterns=[
    path('', views.loginUser, name="index"),
    path('home/', views.home, name="home"),   
    path('register/', views.registerUser, name="registeruser"),
    path('uploadimage/', views.new_image, name="uploadimage"),
    path('viewimage/<int:pk>/', views.viewPhoto, name="viewphoto"),
    path('likes/<int:pk>/', views.likes, name="likes"),
    # path('userprofile/<int:pk>/', views.profile_view, name="userprofile"),
    path("followers/<int:pk>/", views.followers, name="followers"),
    path("editpage/<int:pk>/", views.editpage, name="editprofile"), 
    path("searchprofile/", views.search_profile, name="search_profile"),
    path('logout/', views.logoutUser, name="logout")
]