# Generated by Django 3.2.4 on 2022-07-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0017_auto_20220714_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholder',
            name='health_anms_female',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='health_anms_male',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='health_anms_total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
