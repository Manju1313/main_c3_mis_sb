# Generated by Django 3.2.4 on 2022-08-29 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0035_adolescentfriendlyclub_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adolescentvocationaltraining',
            name='training_providing_by',
        ),
    ]
