# Generated by Django 3.1.5 on 2021-01-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_home', '0003_auto_20210122_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='description',
            field=models.TextField(default='nall', verbose_name='درباره شما'),
            preserve_default=False,
        ),
    ]
