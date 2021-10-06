from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),  
    path('login', views.handLogin, name="login"),
    path("loggedIn",views.loggedIn, name="loggedIn"),
    path("signup_helper",views.signup_page, name="signup_page"),
    path("signup", views.signup_view, name="signup"),

    
]
