from django import template
register = template.Library()

@register.simple_tag
def getValAtIndex(*args, **kwargs):
    val = kwargs['val']
    ind = kwargs['ind']
    return val[int(ind)-1]

@register.simple_tag
def whatIsThat(*args, **kwargs):
    val = kwargs['val']
    return type(val)
