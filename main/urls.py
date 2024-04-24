from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    # path("preference-form/", views.preference_form, name="preference-form"),
    path("dashboard/", views.dashboard, name="dashboard"),
    # path("generate/", views.display_meal_options, name="meal-plan"),  
]