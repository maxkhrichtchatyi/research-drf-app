# Generated by Django 2.2.24 on 2021-10-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210925_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_minutes',
            field=models.SmallIntegerField(),
        ),
    ]
