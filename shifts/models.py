from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Expand user definition"""
    class Meta:
        db_table = 'custom_user'

    hourly_wage = models.IntegerField(verbose_name='Hourly wage', default=0)
    travel_expense = models.IntegerField(verbose_name='Travel expense', default=0)
