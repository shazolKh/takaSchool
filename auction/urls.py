from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.AddProduct, name='addProduct'),
    path('<str:pk>/my-items/', views.MyPostedItems, name='my-items'),
]
