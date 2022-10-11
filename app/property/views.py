from django.shortcuts import render
from property.models import Area
from primary_property.models import PrimaryProperty
# Create your views here.

def index(request):
    queryset = PrimaryProperty.objects.order_by('-click_amount')
    areas = Area.objects.all().values_list('name', flat=True)
    context = {
        'main_complexses': queryset.exclude(logo='')[:10],
        'first_complexses': queryset[:4],
        'areas': areas,
    }
    return render(request, 'property/index.html', context)

def concierge(request):
    return render(request, 'property/concierge.html')

def privacy(request):
    return render(request, 'property/privacy.html')
