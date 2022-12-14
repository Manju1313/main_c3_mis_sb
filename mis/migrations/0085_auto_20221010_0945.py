# Generated by Django 3.2.4 on 2022-10-10 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mis', '0084_auto_20221008_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followup_liaisionmeeting',
            name='department',
        ),
        migrations.CreateModel(
            name='POReportSection17',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Active'), (2, 'Inactive')], db_index=True, default=1)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('suggestions', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createdmis_poreportsection17_related', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modifiedmis_poreportsection17_related', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sites.site')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mis.task')),
            ],
            options={
                'verbose_name_plural': 'CC Report Notes',
            },
        ),
    ]
