"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from home import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('details/<int:id>',views.details,name='details'),
    path('order_data/<int:id>',views.view_order,name='view_order'),
    path('myorders/',views.myorders,name='myorders'),


    #path('kulfi_details/<int:id>',views.kulfi_details,name='kulfi_details'),

    #path('<str:model_name>/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/',views.cart,name='cart'),
    #path('cone/',views.cone,name='cone'),
    #path('bar/',views.bar,name='bar'),
    path('signuppage/',views.signuppage,name='signuppage'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    #path('add_to_cart_kulfi',views.add_to_cart_kulfi,name='add_to_cart_kulfi'),

    path('remove_item/<int:id>',views.remove_item,name='remove_item'),
    path('place_order/<int:id>',views.place_order,name='place_order'),



        



    ]

