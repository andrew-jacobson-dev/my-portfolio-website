# Generated by Django 3.0.5 on 2020-04-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0027_remove_project_t_key_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='i_in_progress',
        ),
        migrations.AlterField(
            model_name='project',
            name='t_code_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
