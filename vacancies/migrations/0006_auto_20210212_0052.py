# Generated by Django 3.1.5 on 2021-02-11 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0005_auto_20210211_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='company',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Владелец',
            ),
        ),
    ]
