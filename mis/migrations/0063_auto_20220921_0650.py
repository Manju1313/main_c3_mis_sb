# Generated by Django 3.2.4 on 2022-09-21 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mis', '0062_reportsection7'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportsection7',
            name='name_of_village',
        ),
        migrations.CreateModel(
            name='ReportSection4a',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Active'), (2, 'Inactive')], db_index=True, default=1)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('name_of_block', models.CharField(blank=True, max_length=250, null=True)),
                ('name_of_panchayat', models.CharField(blank=True, max_length=250, null=True)),
                ('name_of_village', models.CharField(blank=True, max_length=250, null=True)),
                ('name_of_awc_code', models.CharField(blank=True, max_length=250, null=True)),
                ('participated_10_14_years', models.IntegerField(blank=True, null=True)),
                ('bmi_10_14_year', models.IntegerField(blank=True, null=True)),
                ('bmi_15_19_year', models.IntegerField(blank=True, null=True)),
                ('hb_test_10_14_year', models.IntegerField(blank=True, null=True)),
                ('hb_test_15_19_year', models.IntegerField(blank=True, null=True)),
                ('tt_shot_10_14_year', models.IntegerField(blank=True, null=True)),
                ('tt_shot_15_19_year', models.IntegerField(blank=True, null=True)),
                ('counselling_10_14_year', models.IntegerField(blank=True, null=True)),
                ('counselling_15_19_year', models.IntegerField(blank=True, null=True)),
                ('referral_10_14_year', models.IntegerField(blank=True, null=True)),
                ('referral_15_19_year', models.IntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createdmis_reportsection4a_related', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modifiedmis_reportsection4a_related', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sites.site')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mis.task')),
            ],
            options={
                'verbose_name_plural': 'Report Section4a',
            },
        ),
    ]
