# Generated by Django 3.2.4 on 2022-09-20 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0060_reportsection3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportsection3',
            name='number_of_girls_accepted_placement',
        ),
        migrations.RemoveField(
            model_name='reportsection3',
            name='session_name',
        ),
    ]
