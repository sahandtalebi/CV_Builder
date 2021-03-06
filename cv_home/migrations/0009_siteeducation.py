# Generated by Django 3.1.5 on 2021-01-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_home', '0008_sitefun'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.CharField(max_length=30, verbose_name='زمان')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('subject', models.CharField(max_length=200, verbose_name='موضوع')),
                ('description', models.TextField(verbose_name='درباره شما')),
            ],
            options={
                'verbose_name': 'تنظیمات تحصیلات',
                'verbose_name_plural': 'ماژول تحصیلات',
            },
        ),
    ]
