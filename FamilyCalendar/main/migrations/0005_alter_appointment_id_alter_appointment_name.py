# Generated by Django 4.2.7 on 2023-11-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_appointment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(max_length=50, unique_for_year=True),
        ),
    ]