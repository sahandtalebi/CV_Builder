from django.shortcuts import render
from .models import SiteSetting, SiteLink, SiteSkins, SiteFun, SiteEducation, SiteExperience, SiteService


def personal_view(request, *args, **kwargs):
    content = SiteSetting.objects.first()
    links = SiteLink.objects.all()
    skins = SiteSkins.objects.all()
    fun = SiteFun.objects.all()
    context = {
        'baseSetting': content,
        'links': links,
        'skins': skins,
        'fun': fun,
    }
    return render(request, 'sheard/personal.html', context)


def home_page(request):
    content = SiteSetting.objects.first()
    education = SiteEducation.objects.all()
    experience = SiteExperience.objects.all()
    service = SiteService.objects.all()

    context = {
        'baseSetting': content,
        'education': education,
        'experience': experience,
        'service': service
    }

    return render(request, "index.html", context)
