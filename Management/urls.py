"""
URL configuration for Online_Restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('AddItem',views.addItem,name='Add_Item_In_Menu'),
    path('AddMenuItem',views.addMenuItem,name='add_menu_item_form'),
    path('userSignup',views.userSignUp,name='userSignUp'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('userLogout',views.userLogout,name='User Logout'),
    path('manageUsers',views.userManagement,name='User Management'),
    path('delete_user',views.deleteUser,name='User Delete'),
    path('edit_user',views.updateUser,name='User Update'),
    path('media/photo/<str:photo_name>/', views.photo_view, name='photo_view'),
    path('manageMenu', views.MenuManage, name='Mange Menu'),
]
