# Generated by Django 3.1.2 on 2020-11-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20201112_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancies',
            old_name='vacancy_title',
            new_name='job_title',
        ),
        migrations.RemoveField(
            model_name='vacancies',
            name='vacancy_company_id',
        ),
        migrations.RemoveField(
            model_name='vacancies',
            name='vacancy_desc',
        ),
        migrations.RemoveField(
            model_name='vacancies',
            name='vacancy_end_date',
        ),
        migrations.RemoveField(
            model_name='vacancies',
            name='vacancy_start_date',
        ),
        migrations.AddField(
            model_name='vacancies',
            name='job_company',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='vacancies',
            name='job_end_date',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='vacancies',
            name='job_link',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='vacancies',
            name='job_start_date',
            field=models.TextField(default='Null'),
        ),
        migrations.DeleteModel(
            name='Companies',
        ),
    ]