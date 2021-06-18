from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View

from vacancies.forms import ApplicationForm
from vacancies.models import Specialty, Company, Vacancy, Application


class HomeVacancies(TemplateView):
    template_name = 'published/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeVacancies, self).get_context_data(**kwargs)
        context['specialty'] = Specialty.objects.annotate(vacancy_count=Count('vacancies')).filter(vacancy_count__gt=0)
        context['companies'] = Company.objects.annotate(vacancy_count=Count('vacancies')).filter(vacancy_count__gt=0)
        return context


class OneVacancy(View):
    def get(self, request, pk, *args, **kwargs):
        form = ApplicationForm()
        vacancy = get_object_or_404(Vacancy.objects.select_related('company', 'specialty'), pk=pk)
        context = {'form': form, 'vacancy': vacancy}
        return render(request, 'published/vacancy.html', context)

    def post(self, request, pk, *args, **kwargs):
        form = ApplicationForm(request.POST)
        vacancy = get_object_or_404(Vacancy, pk=pk)
        if form.is_valid():
            update_data = form.cleaned_data
            Application.objects.create(
                written_username=update_data['written_username'],
                written_phone=update_data['written_phone'],
                written_cover_letter=update_data['written_cover_letter'],
                vacancy=Vacancy.objects.get(pk=pk),
                user=request.user,
            )
            return redirect('/vacancies/{}/sent'.format(pk))
        context = {'form': form, 'vacancy': vacancy}
        return render(request, 'published/vacancy.html', context)


class OneCompany(TemplateView):
    template_name = "published/company.html"

    def get_context_data(self, pk, **kwargs):
        context = super(OneCompany, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, pk=pk)
        context['vacancies'] = Vacancy.objects.select_related('company').filter(company=context['company'])
        return context


class AllVacancies(ListView):
    template_name = 'published/all_vacancies.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            vacancies = (
                    Vacancy.objects
                    .select_related('company')
                    .filter(Q(title__icontains=query) | Q(skills__icontains=query),
                            )
            )
        else:
            vacancies = Vacancy.objects.select_related('company')
        return vacancies


class VacanciesSpec(TemplateView):
    template_name = "published/vacancies_po_specialty.html"

    def get_context_data(self, slug, **kwargs):
        context = super(VacanciesSpec, self).get_context_data(**kwargs)
        context['specialty'] = get_object_or_404(Specialty, code=slug)
        context['vacancies'] = Vacancy.objects.select_related('company').filter(specialty=context['specialty'])
        return context


def sent(request, pk):
    return render(request, 'sent.html')


def custom_404(request, exception):
    return render(request, "errs/404.html")


def custom_500(request):
    return render(request, "errs/500.html")
