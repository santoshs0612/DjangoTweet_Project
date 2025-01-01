from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name= "index"),
    path('', views.tweetList, name= "tweetList"),
    path('create/', views.tweetCreate, name= "tweetCreate"),
    path('<int:tweetId>/edit/', views.tweetEdit, name= "tweetEdit"),
    path('<int:tweetId>/delete/', views.tweetDelete, name= "tweetDelete"),
    path('register/', views.register, name= "register"),
    
]