# Generated by Django 3.0.5 on 2020-04-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myexperience', '0011_auto_20200413_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='t_company_url',
            field=models.CharField(default='www.acuity.com', max_length=100),
            preserve_default=False,
        ),
    ]
