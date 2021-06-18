from django.contrib import admin

from .models import Vacancy, Company, Specialty, Application, Resume


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'specialty',
        'company',
        'skills',
        'description',
        'salary_min',
        'salary_max',
        'published_date',
    )
    list_filter = ('specialty', 'company', 'published_date')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'location',
        'logo',
        'description',
        'employee_count',
        'owner',
    )
    list_filter = ('owner',)
    search_fields = ('name',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'title_special', 'picture')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'written_username',
        'written_phone',
        'written_cover_letter',
        'vacancy',
        'user',
    )
    list_filter = ('vacancy', 'user')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'status',
        'salary',
        'specialty',
        'grade',
        'education',
        'experience',
        'portfolio',
    )
    list_filter = ('user', 'specialty')
