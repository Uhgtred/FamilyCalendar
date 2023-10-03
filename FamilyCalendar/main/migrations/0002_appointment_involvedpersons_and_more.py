# Generated by Django 4.2.5 on 2023-10-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='involvedPersons',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='dueDate',
            field=models.DateTimeField(),
        ),
    ]