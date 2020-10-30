from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name="signup")
]
