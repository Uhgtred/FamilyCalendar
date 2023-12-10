# Generated by Django 4.2.7 on 2023-12-10 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('name', models.CharField(max_length=10)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.calendar')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.month')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('persons', models.CharField(max_length=100)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.day')),
            ],
        ),
    ]
