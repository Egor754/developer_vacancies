from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from django.views.generic import CreateView

from account.forms import UserRegister, UserLogin


class UserRegisterView(CreateView):
    form_class = UserRegister
    success_url = reverse_lazy('main')
    template_name = 'registration/register.html'


class UserLoginView(LoginView):
    authentication_form = UserLogin
    template_name = 'registration/login.html'
