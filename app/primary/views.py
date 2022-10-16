from django.shortcuts import render, get_object_or_404
from primary import models
from aproperty.models import SiteData
from django.contrib.sites.shortcuts import get_current_site



def index(request, slug):
    obj = get_object_or_404(models.PrimaryProperty, slug=slug)
    site = get_current_site(request)
    site_data = SiteData.objects.get(site=site)
    context = {'obj': obj, 'site': site_data}
    return render(request, 'primary/ru/index.html', context)