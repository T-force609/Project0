from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Admin_site'

urlpatterns =[
    path('Admin_site/', include('admin.site.urls', namespace='Admin_site')),
    path('', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin_site/', views.Admin, name='admin_site'),
    
    
]
