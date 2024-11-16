"""
URL configuration for chocolate_house project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_flavor/', views.add_flavor, name='add_flavor'),
    path('view_flavors/', views.view_flavors, name='view_flavors'),
    path('update_flavor/<int:flavor_id>/', views.update_flavor, name='update_flavor'),
    
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('view_ingredients/', views.view_ingredients, name='view_ingredients'),
    path('update_ingredient/<int:ingredient_id>/', views.update_ingredient, name='update_ingredient'),
    
    path('add_suggestion/', views.add_suggestion, name='add_suggestion'),
    path('view_suggestions/', views.view_suggestions, name='view_suggestions'),
    path('', views.home, name='home'),
]

