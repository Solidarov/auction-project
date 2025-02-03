from django import template

register = template.Library()

@register.filter
def get_price(value):
    """
    Get price from int to float.
    """
    return value / 100