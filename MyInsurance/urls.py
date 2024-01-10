"""
URL configuration for MyInsurance project.

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

from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_policy/', views.create_policy, name='create_policy'),
    path('policy_list/', views.policy_list, name='policy_list'),
    path('create_claim/', views.create_claim, name='create_claim'),
    path('claim_list/', views.claims_list, name='claim_list'),
    path('create_client/', views.create_client, name='create_client'),
    path('client_list/', views.client_list, name='client_list'),
    
    
]
