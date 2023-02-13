from django.http import JsonResponse
from django.shortcuts import render
from aproperty.models import Area, SiteData, LivingType, LivingPropertyType
from primary.models import PrimaryProperty
from resale.models import ResaleProperty
from django.contrib.sites.shortcuts import get_current_site


def index(request):
    s = SiteData.objects.get(site=get_current_site(request))
    queryset = PrimaryProperty.objects.filter(site=s, is_published=True).order_by('-main_order')
    areas = Area.objects.filter(site=s).values_list('name', flat=True)

    rs_count = ResaleProperty.objects.filter(site=s, is_published=True).count()
    context = {
        'main_complexses': queryset.exclude(logo='').filter(logo__isnull=False)[:12],
        'areas': areas,
        'count': queryset.count(),
        'site': s,
        'title_image': s.title_image,
        'slides_count': s.slides.count(),
        'slides': s.slides,
        'site_id': s.site.pk,
        'resale': (rs_count > 0),
        'en': s.is_en(),
        'logo_list': queryset.exclude(logo='').filter(logo__isnull=False).order_by('click_amount'),
        'living_types': LivingType.objects.filter(site=s, ltype=LivingPropertyType.PRIMARY),
        'living_types_resale': LivingType.objects.filter(site=s, ltype=LivingPropertyType.RESALE)
    }
    return render(request, f'aproperty/index.html', context)

def concierge(request):
    s = SiteData.objects.get(site=get_current_site(request))
    context = {
        'site': s, 
        'site_id': s.site.pk,
        'en': s.is_en()
    }
    return render(request, f'aproperty/concierge.html', context)

def privacy(request):
    s = SiteData.objects.get(site=get_current_site(request))
    context = {
        'site': s, 
        'site_id': s.site.pk,
        'en': s.is_en()
    }
    return render(request, f'aproperty/privacy.html', context)


#def index(request):
    #return JsonResponse({'resp': 'OK'})