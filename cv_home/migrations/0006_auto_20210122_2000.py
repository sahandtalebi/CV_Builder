# Generated by Django 3.1.5 on 2021-01-22 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv_home', '0005_sitelink'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitelink',
            options={'verbose_name': 'تنظیمات لینک', 'verbose_name_plural': 'تنظیمات لینک ها'},
        ),
        migrations.AlterModelOptions(
            name='sitesetting',
            options={'verbose_name': 'تنظیمات سایت', 'verbose_name_plural': 'تنظیمات کلی'},
        ),
        migrations.RemoveField(
            model_name='sitelink',
            name='user',
        ),
    ]