# Generated by Django 3.2.4 on 2022-08-30 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application_masters', '0008_trainingsubject'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterLookUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Active'), (2, 'Inactive')], db_index=True, default=1)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=400)),
                ('slug', models.SlugField(blank=True, verbose_name='Slug')),
                ('order', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createdapplication_masters_masterlookup_related', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modifiedapplication_masters_masterlookup_related', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application_masters.masterlookup')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
