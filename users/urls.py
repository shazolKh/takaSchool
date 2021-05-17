from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('dashboard/<str:user>', views.Dashboard, name='dashboard'),
    path('logout/', views.Logout, name='logout'),
]