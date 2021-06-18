from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View

from vacancies.forms import ProfileForm


class ProfileUpdate(LoginRequiredMixin, View):
    def get(self, request):
        profile = get_user_model().objects.get(username=request.user)
        form = ProfileForm(instance=profile)
        context = {'form': form}
        return render(request, 'profile/profile.html', context)

    def post(self, request, *args, **kwargs):
        profile = get_user_model().objects.get(username=request.user)
        form = ProfileForm(request.POST)
        if form.is_valid():
            update_data = form.cleaned_data
            profile.first_name = update_data['first_name']
            profile.last_name = update_data['last_name']
            profile.email = update_data['email']
            profile.save()
            messages.success(request, 'Ваш профиль обновлен')
            redirect('profile')
        context = {'form': form}
        return render(request, 'profile/profile.html', context)
