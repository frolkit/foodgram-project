from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = CreationForm
    success_url = "/"
    template_name = "signup.html"


class SignIn(CreateView):
    form_class = AuthForm
    success_url = "/"
    template_name = "signin.html"


def reset_password():
    pass


def favorites():
    pass


def subscribers():
    pass
