"""
URL configuration for demo project.

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
from django.urls import path,include
from authentication import views as v
from calories import views as v1
from recipes import views as v2
from meals import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('signin/', v.signin, name="signin"),
    path('signup/', v.signup, name="signup"),
    path('signout/', v.signout, name="signout"),
    path('activate/<str:uidb64>/<str:token>/', v.activate, name='activate'),
    path('calories/',v1.calorie_counter,name="calories"),
    path('recipes/',v2.recipes,name="recipes"),
    path('generate-meal-plan/', v3.generate_meal_plan, name="generate-meal-plan"),
]
