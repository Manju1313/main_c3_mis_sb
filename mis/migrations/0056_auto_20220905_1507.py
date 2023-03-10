# Generated by Django 3.2.4 on 2022-09-05 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application_masters', '0012_alter_adolescent_gender'),
        ('mis', '0055_alter_events_name_of_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentvocationaltraining',
            name='training_providing_by',
            field=models.IntegerField(blank=True, choices=[(1, 'JSLPS'), (2, 'SGRS Pvt. Ltd.'), (3, 'Vikas Bharti'), (4, 'Others')], null=True),
        ),
        migrations.AlterField(
            model_name='parentvocationaltraining',
            name='training_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application_masters.trainingsubject'),
        ),
    ]
