# Generated by Django 3.2.18 on 2023-08-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maidapp', '0004_auto_20230813_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='cook',
            name='society_name',
            field=models.CharField(default='Society1', max_length=20),
        ),
        migrations.AddField(
            model_name='maid',
            name='society_name',
            field=models.CharField(default='Society1', max_length=20),
        ),
        migrations.AddField(
            model_name='nanny',
            name='society_name',
            field=models.CharField(default='Society1', max_length=20),
        ),
    ]
