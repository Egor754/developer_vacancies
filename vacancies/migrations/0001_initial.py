# Generated by Django 3.1.5 on 2021-01-29 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('location', models.CharField(max_length=255, verbose_name='Город')),
                ('logo', models.URLField(default='https://place-hold.it/100x60', verbose_name='Логотипчик')),
                ('description', models.TextField(verbose_name='Информация о компании')),
                ('employee_count', models.PositiveIntegerField(verbose_name='Количество сотрудников')),
            ],
            options={
                'verbose_name': 'Компанию',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, verbose_name='Код')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('picture', models.URLField(default='https://place-hold.it/100x60')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('skills', models.CharField(max_length=255, verbose_name='Навыки')),
                ('description', models.TextField(verbose_name='Описание')),
                ('salary_min', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Зарплата от')),
                ('salary_max', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Зарплата до')),
                ('published_at', models.BooleanField(default=True)),
                ('company', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='vacancies',
                    to='vacancies.company',
                    verbose_name='Компания')),
                ('specialty', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='vacancies',
                    to='vacancies.specialty',
                    verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Вакансию',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
