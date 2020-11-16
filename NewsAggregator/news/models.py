from django.db import models


class Vacancies(models.Model):
    job_title = models.CharField(max_length=200)
    job_link = models.TextField(default="Null")
    job_start_date = models.TextField(default="Null")
    job_end_date = models.TextField(default="Null")
    job_company = models.TextField(default="Null")
