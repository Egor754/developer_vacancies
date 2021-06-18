from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.views.generic.base import View

from vacancies.forms import ResumeForm
from vacancies.models import Resume


class ResumeCreate(LoginRequiredMixin, CreateView):
    form_class = ResumeForm
    template_name = 'resume/resume-edit.html'

    def post(self, request, *args, **kwargs):
        form = ResumeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = get_user_model().objects.get(username=request.user)
            form.save()
            messages.success(request, 'Ваше резюме создано')
            return redirect('resume_update')
        context = {'form': form}
        return render(request, 'resume/resume-edit.html', context)


class ResumeUpdate(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            resume = Resume.objects.get(user=request.user)
        except Resume.DoesNotExist:
            return render(request, 'resume/resume-create.html')
        else:
            form = ResumeForm(instance=resume)
            context = {'company': resume, 'form': form}
            return render(request, 'resume/resume-edit.html', context)

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(user=request.user)
        form = ResumeForm(request.POST)
        if form.is_valid():
            update_data = form.cleaned_data
            resume.first_name = update_data['first_name']
            resume.last_name = update_data['last_name']
            resume.status = update_data['status']
            resume.salary = update_data['salary']
            resume.specialty = update_data['specialty']
            resume.grade = update_data['grade']
            resume.education = update_data['education']
            resume.experience = update_data['experience']
            resume.portfolio = update_data['portfolio']
            resume.save()
            messages.success(request, 'Ваше резюме обновлено')
            return redirect('resume_update')
        context = {'form': form}
        return render(request, 'resume/resume-edit.html', context)
