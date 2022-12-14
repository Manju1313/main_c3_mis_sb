# Generated by Django 3.2.4 on 2022-09-22 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
        ('mis', '0067_reportsection10_reportsection2_reportsection8_reportsection9'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportSection6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Active'), (2, 'Inactive')], db_index=True, default=1)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('name_of_block', models.CharField(blank=True, max_length=250, null=True)),
                ('name_of_panchayat', models.CharField(blank=True, max_length=250, null=True)),
                ('name_of_hsc', models.CharField(blank=True, max_length=250, null=True)),
                ('name_of_sahiya_participated', models.CharField(blank=True, max_length=250, null=True)),
                ('no_of_aww', models.CharField(blank=True, max_length=250, null=True)),
                ('girls_10_14_year', models.IntegerField(blank=True, null=True)),
                ('girls_15_19_year', models.IntegerField(blank=True, null=True)),
                ('boys_10_14_year', models.IntegerField(blank=True, null=True)),
                ('boys_15_19_year', models.IntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createdmis_reportsection6_related', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modifiedmis_reportsection6_related', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sites.site')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mis.task')),
            ],
            options={
                'verbose_name_plural': 'Report Section6',
            },
        ),
    ]
