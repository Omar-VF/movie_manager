# Generated by Django 5.0.1 on 2024-02-05 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_alter_movie_data_censor_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='censor_info',
            name='certified_by',
        ),
    ]
