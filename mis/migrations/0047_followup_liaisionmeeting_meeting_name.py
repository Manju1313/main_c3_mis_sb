# Generated by Django 3.2.4 on 2022-09-01 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application_masters', '0009_masterlookup'),
        ('mis', '0046_auto_20220901_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup_liaisionmeeting',
            name='meeting_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='meeting_name', to='application_masters.masterlookup'),
        ),
    ]
