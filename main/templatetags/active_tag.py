from django import template

register = template.Library()

@register.simple_tag
def active(request, view_name):
    if not hasattr(request, 'resolver_match') or not request.resolver_match:
        return ""
    if request.resolver_match.view_name == view_name:
        return ""
    return ""