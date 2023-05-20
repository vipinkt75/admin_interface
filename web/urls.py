from django.urls import path
from . import views


app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("filtter", views.filtter, name="filtter"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
]