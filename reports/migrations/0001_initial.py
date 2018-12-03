# Generated by Django 2.1.3 on 2018-12-03 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_draft', models.BooleanField(default=True, verbose_name='')),
                ('date', models.DateField(default=datetime.date(2018, 12, 3), verbose_name='日付')),
                ('opening_time', models.TimeField(default=datetime.time(11, 0), verbose_name='開始時間')),
                ('closing_time', models.TimeField(default=datetime.time(19, 0), verbose_name='終了時間')),
                ('recess', models.TimeField(default=datetime.time(1, 0), verbose_name='休憩時間')),
                ('feeling', models.CharField(max_length=255, verbose_name='気分')),
                ('core_value', models.CharField(max_length=255, verbose_name='意識したcore value')),
                ('done', models.TextField(verbose_name='やったこと')),
                ('todo', models.TextField(verbose_name='次やること')),
                ('review', models.TextField(verbose_name='フリー記述欄（振り返りや感想）')),
            ],
            options={
                'db_table': 'report',
            },
        ),
    ]
