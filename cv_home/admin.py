from django.contrib import admin
from django.contrib.auth.models import Group

from .models import SiteSetting, SiteLink, SiteSkins, SiteFun, SiteEducation, SiteExperience, SiteService

admin.site.unregister(Group)

admin.site.register(SiteSetting)
admin.site.register(SiteLink)
admin.site.register(SiteSkins)
admin.site.register(SiteFun)
admin.site.register(SiteEducation)
admin.site.register(SiteExperience)
admin.site.register(SiteService)
