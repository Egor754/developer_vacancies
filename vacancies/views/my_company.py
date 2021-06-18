from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from django.views.generic.base import View

from vacancies.forms import MyCompany, MyVacancy
from vacancies.models import Company, Vacancy, Application


class UserCompanyCreate(LoginRequiredMixin, CreateView):
    form_class = MyCompany
    template_name = 'my_company/company-edit.html'
    slug_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        form = MyCompany(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = get_user_model().objects.get(username=request.user)
            form.save()
            messages.success(request, 'Ваша компания успешно создана')
            return redirect('company_update')
        context = {'form': form}
        return render(request, 'my_company/company-edit.html', context)


class UserCompanyUpdate(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(owner__username=request.user)
        except Company.DoesNotExist:
            return render(request, 'my_company/company-create.html')
        else:
            form = MyCompany(instance=company)
            context = {'company': company, 'form': form}
            return render(request, 'my_company/company-edit.html', context)

    def post(self, request, *args, **kwargs):
        company = Company.objects.get(owner__username=request.user)
        form = MyCompany(request.POST, request.FILES)
        if form.is_valid():
            update_data = form.cleaned_data
            company.name = update_data['name']
            company.location = update_data['location']
            company.logo = update_data['logo'] if update_data['logo'] else company.logo
            company.description = update_data['description']
            company.employee_count = update_data['employee_count']
            company.save()
            messages.success(request, 'Информация о компании обновлена')
            return redirect('company_update')
        context = {'form': form}
        return render(request, 'my_company/company-edit.html', context)


class UserVacanciesUpdate(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        application = Application.objects.filter(vacancy=pk)
        form = MyVacancy(instance=vacancy)
        context = {'form': form, 'vacancy': vacancy, 'applications': application}
        return render(request, 'my_company/vacancy-edit.html', context)

    def post(self, request, pk, *args, **kwargs):
        vacancy = Vacancy.objects.get(pk=pk)
        form = MyVacancy(request.POST)
        if form.is_valid():
            update_data = form.cleaned_data
            vacancy.title = update_data['title']
            vacancy.specialty = update_data['specialty']
            vacancy.skills = update_data['skills']
            vacancy.description = update_data['description']
            vacancy.salary_min = update_data['salary_min']
            vacancy.salary_max = update_data['salary_max']
            vacancy.save()
            messages.success(request, 'Информация о вакансии обновлена')
        context = {'form': form, 'vacancy': vacancy}
        return render(request, 'my_company/vacancy-edit.html', context)


class MyVacancies(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.prefetch_related('applications').filter(company__owner=request.user)
        context = {'vacancies': vacancies}
        return render(request, 'my_company/vacancy-list.html', context)


class MyVacancyCreate(LoginRequiredMixin, CreateView):
    form_class = MyVacancy
    template_name = 'my_company/vacancy-edit.html'

    def post(self, request, *args, **kwargs):
        form = MyVacancy(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.company = Company.objects.get(owner__username=request.user)
            form.save()
            return redirect('my_vacancies')
        context = {'form': form}
        return render(request, 'my_company/company-edit.html', context)
