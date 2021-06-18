from django.urls import path
from vacancies.views.my_company import UserCompanyUpdate, UserCompanyCreate, UserVacanciesUpdate, MyVacancies, \
    MyVacancyCreate
from vacancies.views.profile import ProfileUpdate
from vacancies.views.published import HomeVacancies, OneVacancy, OneCompany, AllVacancies, VacanciesSpec, sent
from vacancies.views.resume import ResumeCreate, ResumeUpdate

urlpatterns = [
    path('', HomeVacancies.as_view(), name='main'),
    path('vacancies/<slug:pk>/', OneVacancy.as_view(), name='vacancy'),
    path('companies/<slug:pk>/', OneCompany.as_view(), name='company'),
    path('vacancies/', AllVacancies.as_view(), name='vacancies'),
    path('vacancies/<slug:pk>/sent/', sent, name='sent'),
    path('vacancies/cat/<slug:slug>/', VacanciesSpec.as_view(), name='special'),
    path('mycompany/', UserCompanyUpdate.as_view(), name='company_update'),
    path('mycompany/create', UserCompanyCreate.as_view(), name='my_company'),
    path('mycompany/vacancies/<int:pk>/', UserVacanciesUpdate.as_view(), name='my_one_vacancy'),
    path('mycompany/vacancies/', MyVacancies.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/create', MyVacancyCreate.as_view(), name='vacancies_create'),
    path('myresume/create', ResumeCreate.as_view(), name='resume_create'),
    path('myresume/', ResumeUpdate.as_view(), name='resume_update'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]
