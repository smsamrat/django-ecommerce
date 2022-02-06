from atexit import register
from django import template
from store.models import LogoInfo, favicon

register = template.Library()

@register.filter
def logo(user):
    if user.is_authenticated:
        logo = LogoInfo.objects.filter(user=user, is_active=True).order_by('-id').first()
        print(logo)
        return logo.image.url

    else:
        logo = LogoInfo.objects.filter(is_active=True).order_by('-id').first()
        return logo.image.url

@register.filter
def faviconInfo(user):
    if user.is_authenticated:
        faviconInfo = favicon.objects.filter(user=user, is_active=True).order_by('-id').first()
        print(faviconInfo)
        return faviconInfo.image.url

    else:
        faviconInfo = favicon.objects.filter(is_active=True).order_by('-id').first()
        return faviconInfo.image.url


