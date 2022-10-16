from django.shortcuts import render
from aproperty.models import Area, SiteData
from primary.models import PrimaryProperty
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.

def index(request):
    site = get_current_site(request)
    site_data = SiteData.objects.get(site=site)
    queryset = PrimaryProperty.objects.filter(site=site_data).order_by('main_order')
    areas = Area.objects.all().values_list('name', flat=True)
    context = {
        'main_complexses': queryset.exclude(logo='')[:10],
        'areas': areas,
        'count': queryset.count(),
        'site': site_data
    }
    return render(request, 'aproperty/ru/index.html', context)

def concierge(request):
    return render(request, 'aproperty/concierge.html')

def privacy(request):
    return render(request, 'aproperty/privacy.html')
