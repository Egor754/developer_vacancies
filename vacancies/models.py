from django.contrib.auth.models import User
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from employment.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название вакансии')
    specialty = models.ForeignKey(
        'Specialty',
        verbose_name='Специализация',
        on_delete=models.CASCADE,
        related_name="vacancies",
    )
    company = models.ForeignKey(
        'Company',
        verbose_name='Компания',
        on_delete=models.CASCADE,
        related_name="vacancies",
    )
    skills = models.CharField(max_length=255, verbose_name='Навыки')
    description = models.TextField(verbose_name='Описание')
    salary_min = models.PositiveIntegerField(verbose_name='Зарплата от')
    salary_max = models.PositiveIntegerField(verbose_name='Зарплата до')
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    location = models.CharField(max_length=255, verbose_name='Город')
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, verbose_name='Логотипчик')
    description = models.TextField(verbose_name='Информация о компании')
    employee_count = models.PositiveIntegerField(verbose_name='Количество сотрудников')
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Владелец', related_name="company")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компанию'
        verbose_name_plural = 'Компании'


class Specialty(models.Model):
    code = models.CharField(max_length=255, verbose_name='Код')
    title_special = models.CharField(max_length=255, verbose_name='Название')
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR, verbose_name='Логотипчик')

    def __str__(self):
        return self.title_special

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Application(models.Model):
    written_username = models.CharField(max_length=255, verbose_name='Имя')
    written_phone = PhoneNumberField(unique=True, verbose_name='Телефон')
    written_cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications",
                                verbose_name='Вакансия')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications", verbose_name='Пользователь')

    def __str__(self):
        return f'Отклик от {self.written_username}'

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'


class Resume(models.Model):
    not_work = 'not'
    offers = 'consider'
    seek_work = 'seek'
    ready_work = [
        (not_work, 'Не ищу работу'),
        (offers, 'Рассматриваю предложения'),
        (seek_work, 'Ищу работу'),
    ]
    intern = 'intern'
    junior = 'junior'
    middle = 'middle'
    senior = 'senior'
    lead = 'lead'
    qualification = [
        (intern, 'Стажер'),
        (junior, 'Джуниор'),
        (middle, 'Миддл'),
        (senior, 'Синьор'),
        (lead, 'Лид'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="resume", verbose_name='Пользователь')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    status = models.CharField(max_length=15, choices=ready_work, default=not_work, verbose_name='Готовность к работе')
    salary = models.PositiveIntegerField(verbose_name='Вознаграждение')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='specialty',
                                  verbose_name='Специализация')
    grade = models.CharField(max_length=20, choices=qualification, default=intern, verbose_name='Квалификация')
    education = models.TextField(verbose_name='Образование', blank=True, default='')
    experience = models.TextField(verbose_name='Опыт работы', blank=True, default='')
    portfolio = models.URLField(verbose_name='Портфолио', blank=True, default='')

    def __str__(self):
        return f'Резюме {self.user}'

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
