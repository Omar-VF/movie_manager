# Generated by Django 5.0.1 on 2024-01-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_data_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_data',
            name='poster',
            field=models.ImageField(blank=True, default='images/UnavailableImg.png', upload_to='images/'),
        ),
    ]