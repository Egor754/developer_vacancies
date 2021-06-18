from django.contrib.auth import get_user_model
from django.forms import ModelForm

from vacancies.models import Company, Vacancy, Application, Resume


class MyCompany(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count']


class MyVacancy(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max']


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['first_name', 'last_name', 'status', 'salary', 'specialty', 'grade', 'education', 'experience',
                  'portfolio']


class ProfileForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
