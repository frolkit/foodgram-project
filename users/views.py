from django.views.generic import CreateView
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = "/accounts/login/"
    template_name = "signup.html"


class 