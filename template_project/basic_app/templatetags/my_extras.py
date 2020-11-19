from django import template

register = template.Library()

@register.filter
def cut_ex(value, arg):
    """
    this cuts out all values of "arg" from the string!
    """

    return value.replace(arg, '')