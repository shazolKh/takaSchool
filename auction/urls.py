from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.AddProduct, name='addProduct'),
    path('<str:pk>/my-items/', views.MyPostedItems, name='my-items'),
    path('bid/<str:pk>/', views.BidPlace, name='bid'),
    path('edit-bid/<str:pk>/', views.EditBid, name='edit'),
]
