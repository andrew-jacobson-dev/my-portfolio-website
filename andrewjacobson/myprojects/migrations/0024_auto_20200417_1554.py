# Generated by Django 3.0.5 on 2020-04-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0023_auto_20200417_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='t_image_path',
            field=models.FilePathField(path='img/'),
        ),
    ]