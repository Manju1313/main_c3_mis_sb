# Generated by Django 3.2.4 on 2022-09-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0074_historyrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyrecord',
            name='end_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
