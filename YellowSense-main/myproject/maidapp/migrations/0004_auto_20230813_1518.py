# Generated by Django 3.2.18 on 2023-08-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maidapp', '0003_auto_20230813_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='house_size',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='other_services',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='services_required',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='timings',
        ),
        migrations.AddField(
            model_name='customer',
            name='additional_data',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='customer',
            name='preferred_gender',
            field=models.CharField(default='Any', max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='selected_service',
            field=models.CharField(default='Maid', max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='society_name',
            field=models.CharField(default='Society2', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='timings_from',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='timings_to',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='additional_requirements',
            field=models.TextField(null=True),
        ),
    ]
