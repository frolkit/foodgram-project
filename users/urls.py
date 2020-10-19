from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("password_change/",
         auth_views.PasswordChangeView.as_view(template_name="registration/password_change"),
         name="password_change"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
]
