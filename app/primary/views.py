from django.shortcuts import render, get_object_or_404
from primary import models
from aproperty.models import SiteData
from django.contrib.sites.shortcuts import get_current_site



def index(request, slug):
    s = SiteData.objects.get(site=get_current_site(request))
    obj = get_object_or_404(models.PrimaryProperty, slug=slug, site=s, is_published=True)
    obj.click_amount += 1; obj.save()

    context = {'obj': obj, 'site': s, 'site_id': s.site.pk}
    return render(request, f'primary/{s.get_lan()}/index.html', context)