# Generated by Django 4.0.3 on 2022-03-29 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_ispublished_alter_movie_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image_itself',
            field=models.FileField(default='1.jpeg', upload_to='img'),
            preserve_default=False,
        ),
    ]