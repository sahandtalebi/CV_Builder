# Generated by Django 3.1.5 on 2021-01-22 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cv_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesetting',
            options={'verbose_name': 'تنظیمات سایت', 'verbose_name_plural': 'ماژول تنظیمات'},
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='Location',
            field=models.CharField(default='null', max_length=100, verbose_name='محل زندگی شما'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, verbose_name='ایمیل شما'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='name',
            field=models.CharField(default=12, max_length=150, verbose_name='نام کامل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='شما تلفن'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='photo',
            field=models.ImageField(default=1, upload_to='', verbose_name='عکس شما'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='your_job',
            field=models.CharField(blank=True, max_length=150, null=None, verbose_name='شغل شما'),
        ),
    ]