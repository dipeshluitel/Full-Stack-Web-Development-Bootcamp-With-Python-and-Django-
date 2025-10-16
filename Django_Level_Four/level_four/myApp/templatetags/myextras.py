from django import template
register = template.Library()

@register.filter(name = 'em')
def em(value):
    return f"<em>{value}</em>"