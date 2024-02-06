# Generated by Django 5.0.1 on 2024-02-06 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_remove_censor_info_certified_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_data',
            name='directed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directed_by', to='movies.director'),
        ),
    ]
