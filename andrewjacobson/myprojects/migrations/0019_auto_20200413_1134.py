# Generated by Django 3.0.5 on 2020-04-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0018_auto_20200413_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='t_image_path',
            field=models.FilePathField(path='/img'),
        ),
    ]