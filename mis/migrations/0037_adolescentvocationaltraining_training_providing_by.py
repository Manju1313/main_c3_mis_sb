# Generated by Django 3.2.4 on 2022-08-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0036_remove_adolescentvocationaltraining_training_providing_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='adolescentvocationaltraining',
            name='training_providing_by',
            field=models.IntegerField(blank=True, choices=[(1, 'JSLPS'), (2, 'SGRS Pvt. Ltd.'), (3, 'Vikas Bharti'), (4, 'Others')], null=True),
        ),
    ]