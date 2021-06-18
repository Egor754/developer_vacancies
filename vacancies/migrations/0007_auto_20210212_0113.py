# Generated by Django 3.1.5 on 2021-02-11 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_auto_20210212_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='applications',
                to='vacancies.vacancy',
                verbose_name='Вакансия',
            ),
        ),
    ]
