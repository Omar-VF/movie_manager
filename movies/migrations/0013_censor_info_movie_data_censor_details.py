# Generated by Django 5.0.1 on 2024-02-05 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_movie_data_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='censor_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=10)),
                ('certified_by', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie_data',
            name='censor_details',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie', to='movies.censor_info'),
        ),
    ]