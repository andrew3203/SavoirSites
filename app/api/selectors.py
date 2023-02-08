from aproperty import models
from rest_framework.exceptions import NotFound


def site_get(site_domain: str) -> models.SiteData:
    try:
        site = models.Site.objects.get(domain=site_domain)
        return models.SiteData.objects.get(site=site)
    except models.Site.DoesNotExist:
        raise NotFound
