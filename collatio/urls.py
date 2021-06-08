from django.urls import path
from . import views

#add all url paths here

urlpatterns = [
    path('', views.home, name="home"),
    path('search/<str:primaryKey>/', views.search, name="search"),
    path('category/', views.categories, name="category"),
    path('product/<str:pk>', views.productDetails, name='product'),
    path('all_products', views.allProducts, name='all_products'),
]