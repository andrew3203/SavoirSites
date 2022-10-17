from django.shortcuts import render
from aproperty.models import Area, SiteData
from primary.models import PrimaryProperty
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.

def index(request):
    s = SiteData.objects.get(site=get_current_site(request))
    queryset = PrimaryProperty.objects.filter(site=s).order_by('main_order')
    areas = Area.objects.filter(site=s).values_list('name', flat=True)
    context = {
        'main_complexses': queryset.exclude(logo='')[:10],
        'areas': areas,
        'count': queryset.count(),
        'site': s,
        'title_image': s.title_image,
        'slides_count': s.slides.count(),
        'slides': s.slides,
        'site_id': s.site.pk
    }
    return render(request, f'aproperty/{s.get_lan()}/index.html', context)

def concierge(request):
    s = SiteData.objects.get(site=get_current_site(request))
    return render(request, 'aproperty/{s.get_lan()}/concierge.html', {'site': s, 'site_id': s.site.pk})

def privacy(request):
    s = SiteData.objects.get(site=get_current_site(request))
    return render(request, 'aproperty/{s.get_lan()}/privacy.html', {'site': s, 'site_id': s.site.pk})
