from resale import models
from rest_framework.exceptions import NotFound



def resaleList_get(*args, **kwargs) -> models.ResaleProperty:
    try:
        site_id = int(kwargs['site_id'][0])
        kwargs.pop('site_id')
    except:
        raise NotFound

    return models.ResaleProperty.objects.filter(
        site__site__id=site_id,
        is_published=True, 
    )

def resaleRecomend_get(*args, **kwargs) -> models.ResaleProperty:
    try:
        site_id = int(kwargs['site_id'][0])
        kwargs.pop('site_id')
    except:
        raise NotFound

    return models.ResaleProperty.objects.filter(
        site__site__id=site_id,
        is_published=True,
    ).order_by('click_amount')[:20]

def resale_get(id: str) -> models.ResaleProperty:
    try:
        return models.ResaleProperty.objects.get(id=int(id))
    except:
        raise NotFound