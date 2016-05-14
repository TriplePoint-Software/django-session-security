from django import template

from session_security.models import SessionSecurityConfiguration

register = template.Library()


@register.filter
def expire_after(request):
    return SessionSecurityConfiguration.get_solo().expire_after


@register.filter
def warn_after(request):
    return SessionSecurityConfiguration.get_solo().warn_after
