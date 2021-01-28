from django.contrib.auth.models import User
from django.db import models


class SiteSetting(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام کامل')
    datetime = models.CharField(max_length=150, verbose_name='تاریخ تولد')
    your_job = models.CharField(max_length=150, verbose_name='شغل شما')
    photo = models.ImageField(verbose_name='عکس شما')
    phone = models.IntegerField(null=True, verbose_name='شما تلفن')
    Location = models.CharField(max_length=100, verbose_name='محل زندگی شما')
    email = models.EmailField(verbose_name='ایمیل شما')
    description = models.TextField(verbose_name='درباره شما')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات کلی'

    def __str__(self):
        return self.name


class SiteLink(models.Model):
    user = models.ManyToOneRel(User, field_name='icon', to='icon')
    name = models.CharField(max_length=100, verbose_name='نام')
    icon = models.CharField(max_length=100, verbose_name='ای دی ایکون')
    link = models.CharField(max_length=500, verbose_name='لینک')

    class Meta:
        verbose_name = 'تنظیمات لینک'
        verbose_name_plural = 'تنظیمات لینک ها'

    def __str__(self):
        return self.name


class SiteSkins(models.Model):
    user = models.ManyToOneRel(User, field_name='name', to='name')
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'تنظیمات مهارت'
        verbose_name_plural = 'تنظیمات مهارت ها'

    def __str__(self):
        return self.name


class SiteFun(models.Model):
    user = models.ManyToOneRel(User, field_name='name', to='name')
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'تنظیمات سرگرمی'
        verbose_name_plural = 'تنظیمات سرگرمی ها'

    def __str__(self):
        return self.name


class SiteEducation(models.Model):
    user = models.ManyToOneRel(User, field_name='name', to='name')
    date_time = models.CharField(max_length=30, verbose_name='زمان')
    name = models.CharField(max_length=200, verbose_name='نام')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    description = models.TextField(verbose_name='درباره شما')
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'تنظیمات تحصیلات'
        verbose_name_plural = 'ماژول تحصیلات'

    def __str__(self):
        return self.name


class SiteExperience(models.Model):
    user = models.ManyToOneRel(User, field_name='name', to='name')
    date_time = models.CharField(max_length=30, verbose_name='زمان')
    name = models.CharField(max_length=200, verbose_name='نام تیم یا شرکت')
    subject = models.CharField(max_length=200, verbose_name='نوع فعالیت')
    description = models.TextField(verbose_name='توضیحات')
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'تنظیمات تجربه'
        verbose_name_plural = 'ماژول تجربه'

    def __str__(self):
        return self.name


class SiteService(models.Model):
    user = models.ManyToOneRel(User, field_name='name', to='name')
    name = models.CharField(max_length=200, verbose_name='نام مدرک')
    icon = models.ImageField(max_length=100, verbose_name='عکس')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'تنظیمات مدارک'
        verbose_name_plural = 'ماژول مدارک'

    def __str__(self):
        return self.name
