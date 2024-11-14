# Generated by Django 3.2.4 on 2022-10-08 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0081_auto_20220930_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='champions',
            name='fourth_inst_visited',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'CHC'), (2, 'AFHC'), (3, 'HSC'), (4, 'HWC'), (5, 'Police Station'), (6, 'Post Office'), (7, 'Bank'), (8, 'Pragya Kendra'), (9, 'Panchayat Bhawan'), (10, 'Employment exchange'), (11, 'Zoo'), (12, 'Science Park'), (13, 'Others')], null=True),
        ),
    ]
