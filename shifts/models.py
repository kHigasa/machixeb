import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Expand user definition"""

    class Meta:
        db_table = 'custom_user'

    hourly_wage = models.IntegerField(verbose_name='時給', default=0)
    travel_expense = models.IntegerField(verbose_name='交通費（片道）', default=0)


class Shift(models.Model):
    """Shift model"""

    class Meta:
        db_table = 'shift'

    date = models.DateField(verbose_name='日付')
    opening_time = models.TimeField(verbose_name='開始時間', default=datetime.time(11, 0, 0))
    closing_time = models.TimeField(verbose_name='終了時間', default=datetime.time(19, 0, 0))

    def __str__(self):
        return self.date
