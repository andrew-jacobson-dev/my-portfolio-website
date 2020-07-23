# Generated by Django 3.0.5 on 2020-05-10 09:11

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_image_path', models.ImageField(upload_to='images/')),
                ('t_interests', tinymce.models.HTMLField()),
                ('t_details', tinymce.models.HTMLField()),
            ],
        ),
    ]
