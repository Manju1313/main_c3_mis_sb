# Generated by Django 3.2.4 on 2022-07-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0023_auto_20220719_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boysahwd',
            name='tt_10_14_years',
        ),
        migrations.RemoveField(
            model_name='boysahwd',
            name='tt_15_19_years',
        ),
        migrations.AddField(
            model_name='events',
            name='name_of_visited',
            field=models.IntegerField(blank=True, choices=[(1, 'Village'), (2, 'AWC'), (3, 'School')], null=True),
        ),
        migrations.AddField(
            model_name='sessionmonitoring',
            name='name_of_visited',
            field=models.IntegerField(blank=True, choices=[(1, 'Village'), (2, 'AWC'), (3, 'School')], null=True),
        ),
        migrations.AlterField(
            model_name='sessionmonitoring',
            name='session_attended',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
