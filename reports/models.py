import datetime
from django.db import models


class Report(models.Model):
    """Report model"""

    class Meta:
        db_table = 'report'

    is_draft = models.BooleanField(verbose_name='', default=True)
    date = models.DateField(verbose_name='日付', default=datetime.date.today())
    opening_time = models.TimeField(verbose_name='開始時間', default=datetime.time(11, 0, 0))
    closing_time = models.TimeField(verbose_name='終了時間', default=datetime.time(19, 0, 0))
    recess = models.TimeField(verbose_name='休憩時間', default=datetime.time(1, 0, 0))
    feeling = models.CharField(verbose_name='気分')
    core_value = models.CharField(verbose_name='意識したcore value')
    done = models.TextField(verbose_name='やったこと')
    todo = models.TextField(verbose_name='次やること')
    review = models.TextField(verbose_name='フリー記述欄（振り返りや感想）')

    def __str__(self):
        return self.feeling
