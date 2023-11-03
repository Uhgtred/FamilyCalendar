# Generated by Django 4.2.7 on 2023-11-03 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_appointment_duedate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='calendar',
            name='name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='dueDate',
            field=models.DateTimeField(default=datetime.date(2023, 11, 3), verbose_name=datetime.date(2023, 11, 3)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='involvedPersons',
            field=models.CharField(default='Niemand', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='name',
            field=models.CharField(default='Termin', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calendar',
            name='year',
            field=models.IntegerField(default=2023),
            preserve_default=False,
        ),
    ]
