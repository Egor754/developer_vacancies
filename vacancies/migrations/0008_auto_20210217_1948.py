# Generated by Django 3.1.5 on 2021-02-17 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0007_auto_20210212_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='applications',
                to='vacancies.vacancy',
                verbose_name='Вакансия',
            ),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to='speciality_images', verbose_name='Логотипчик'),
        ),
    ]
