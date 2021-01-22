from django.shortcuts import render
from .models import SiteSetting, SiteLink, SiteSkins, SiteFun, SiteEducation


def home_page(request):
    content = SiteSetting.objects.first()
    links = SiteLink.objects.all()
    skins = SiteSkins.objects.all()
    fun = SiteFun.objects.all()
    education = SiteEducation.objects.all()
    context = {
        'baseSetting': content,
        'links': links,
        'skins': skins,
        'fun': fun,
        'education': education
    }

    return render(request, "index.html", context)
