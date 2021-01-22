from django.contrib import admin
from .models import SiteSetting, SiteLink, SiteSkins, SiteFun, SiteEducation

admin.site.register(SiteSetting)
admin.site.register(SiteLink)
admin.site.register(SiteSkins)
admin.site.register(SiteFun)
admin.site.register(SiteEducation)
