# Generated by Django 3.1.2 on 2020-11-12 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20201112_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancies',
            old_name='vacancy_company',
            new_name='vacancy_company_id',
        ),
    ]
