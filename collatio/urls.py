from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('category/', views.categories, name="category"),
]