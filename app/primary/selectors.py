from primary import models
from rest_framework.exceptions import NotFound



def primaryList_get(*args, **kwargs) -> models.PrimaryProperty:
    try:
        site_id = int(kwargs['site_id'][0])
        kwargs.pop('site_id')
    except:
        raise NotFound

    return models.PrimaryProperty.objects.filter(
        site__site__id=site_id,
        is_published=True, 
    )

def primaryRecomend_get(*args, **kwargs) -> models.PrimaryProperty:
    try:
        site_id = int(kwargs['site_id'][0])
        kwargs.pop('site_id')
    except:
        raise NotFound

    return models.PrimaryProperty.objects.filter(
        site__site__id=site_id,
        is_published=True,
    ).order_by('click_amount')[:20]

def primary_get(id: str) -> models.PrimaryProperty:
    try:
        return models.PrimaryProperty.objects.get(id=int(id))
    except:
        raise NotFound