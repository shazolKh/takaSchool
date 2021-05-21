from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('admin/', views.AdminLogin, name='admin-login'),
    path('login/', views.Login, name='login'),
    path('dashboard/<str:user>', views.Dashboard, name='dashboard'),
    path('logout/', views.Logout, name='logout'),
    path('admin-dashboard', views.AdminDashboard, name='admin-dashboard'),
    path('chart-date/', views.Chart, name='chart-date'),
]
